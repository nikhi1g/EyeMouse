import cv2
from gaze_tracking import GazeTracking
from time import sleep
import pyautogui
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

confcounter = 0

click = False
left = False
right = False
center = False


while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
        right = True
    if gaze.is_left():
        text = "Looking left"
        left = True
    if gaze.is_center():
        text = "Looking center"
        center = True
    if gaze.is_blinking():
        text = "Blinking"
        click = True

    if click:
        confcounter += 1
        click = False
        if confcounter > 3:
            print("click")
            pyautogui.click()
            click = False
            confcounter = 0



    cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", new_frame)

    if cv2.waitKey(1) == 27:
        break