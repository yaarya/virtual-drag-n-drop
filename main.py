import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector as HD
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HD(detectionCon=0)

colorR = (0, 100, 255)

class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size
    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # if index tip is in rectangle
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor

rectList = []
for x in range(5):
    rectList.append(DragRect([x*250+150, 150]))


while True:
    success, img = cap.read()

    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l, _, _ = detector.findDistance(8, 12, img, draw=False)
        print(l)
        if l < 40:
            cursor = lmList[8]
            #call update
            for rect in rectList:
                rect.update(cursor)
        else:
            colorR = (0, 100, 255)

    # to draw transparent rectangle
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)

        cvzone.cornerRect(imgNew, (cx-w//2, cy-h//2, w, h), 20, rt=0)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1-alpha, 0)[mask]

    # to draw solid rectangle
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w, h = rect.size
    #     cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)
    #
    #     cvzone.cornerRect(img, (cx-w//2, cy-h//2, w, h), 20, rt=0)

    cv2.imshow("Image", out)
    cv2.waitKey(1)