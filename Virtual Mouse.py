#Library imports
import cv2
import mediapipe as mp
import pyautogui

#Main Code
check_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
video = cv2.VideoCapture(0)     #Capturing from the first video source (native web cam or the first camera of device)
screen_height, screen_width = pyautogui.size()
while True:
    _, frame = video.read()     #first variable is not required in this case as it will return a boolean whether a frame is returned or not
    frame = cv2.flip(frame,1)   #flip the image as the output is mirrored also 1 means to flip around y axis
    frame_height, frame_width,_ = frame.shape 
    color_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)     #just converting the frame captured to rgb format (you can also convert it into grayscale depends on you)
    result = check_hands.process(frame)
    hands = result.multi_hand_landmarks
    
    if hands:
       
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    x_new = screen_width/frame_width * x
                    y_new = screen_height/frame_height * y
                    cv2.circle(img = frame, center=(x,y), radius=30, color=(0,255,0))
                    pyautogui.moveTo(x_new,y_new)
                
                
                if id == 12:
                    middle_x = screen_width/frame_width * x
                    middle_y = screen_height/frame_height * y
                    cv2.circle(img = frame, center=(x,y), radius=30, color=(0,255,0))
                    
                    if abs(middle_y - y_new) < 10:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Hand Controlled Mouse',frame)
    cv2.waitKey(1)