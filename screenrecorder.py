import cv2
import numpy as np 
import pyautogui
SCREEN_SIZE = (1920, 1080)
forucc = cv2.VideoWriter_forucc(*"XVID")
out = cv2.VideoWriter("output.avi", forucc, 20.0, (SCREEN_SIZE))
while True: 

    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
           break 
cv2.destroyALLWindows()
out.relase()    
