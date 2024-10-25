# Hand Tracking Drag and Drop Rectangles

This project demonstrates a simple application of hand tracking using OpenCV and the CVZone library. The application allows users to drag and drop rectangles on the screen using their hand movements.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Features

- Real-time hand tracking using a webcam.
- Ability to drag and reposition rectangles with your index finger.
- Transparent overlay effect for visual feedback.
- Customizable rectangle properties (size and position).

## Requirements

To run this project, you will need:

- Python 3.x
- OpenCV
- NumPy
- CVZone

- You can install the required libraries using pip:

  ```bash
  pip install opencv-python numpy cvzone

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/hand-tracking-drag-drop.git
   cd hand-tracking-drag-drop

2. **Install required dependencies as mentioned above.**

## Usage
- Connect a webcam to your computer.
- Run the script:
  ```bash
  python main.py
- Position your hand in front of the camera. Use your index finger to drag the rectangles around the screen.

## Code Explanation
The main components of the code are as follows:
- HandDetector: This class from CVZone is used to detect hands and track finger positions.
- DragRect Class: This class represents a draggable rectangle. It has methods to update its position based on the cursor's location (the tip of the index finger).
- Main Loop:
- - Captures video frames from the webcam.
- - Flips the image for a mirror effect.
- - Detects hands and finds keypoints (landmarks) of the fingers.
- - Checks if the index finger is close enough to any rectangle to initiate dragging.
- - Updates rectangle positions based on finger movement.
- - Renders transparent rectangles over the video feed.


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you wish!
