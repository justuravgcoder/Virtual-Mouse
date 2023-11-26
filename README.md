# HandGestureMouseControl

## Overview

This project allows you to control your computer's mouse in real-time using hand gestures. By leveraging computer vision and hand tracking, you can move the mouse pointer and perform clicks simply by moving your hand.

## Installation

To use this project, you'll need to install the following Python libraries:

```bash
pip install mediapipe
pip install pyautogui
pip install opencv-python
```
## Library Descriptions
<ul>
<li>opencv: Used to capture video frames, essential for real-time hand tracking.</li>
<li>mediapipe: Enables the extraction of hand landmarks, crucial for determining hand gestures.</li>
<li>pyautogui: Facilitates mouse control and click operations.</li>
</ul>
## How to Use
<ol>
<li>Make sure you have a webcam connected to your computer.</li>
<li>Run the script.</li>
<li>Position your hand in front of the webcam, and the program will detect it.</li>
<li>Move your hand to control the mouse pointer.</li>
<li>To perform a click operation, lower your middle finger until it almost resembles the height of the pointer finger.</li>
</ol>

## Additional Notes
<ol>
<li>Experiment with different hand gestures to explore additional mouse control functionalities.</li>
<li>Ensure proper lighting and hand visibility for optimal performance.</li>
<li>Have fun and get creative with how you interact with your computer!</li>
</ol>
## Acknowledgments
This project uses the following open-source libraries: mediapipe, pyautogui, opencv.
Feel free to contribute, report issues, or suggest improvements!
