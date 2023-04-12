import mouseinfo
from matplotlib import pyplot as plt

print("hhh")
import cv2
import mediapipe as mp
import time
#import pyautogui as p
from pynput.mouse import Button, Controller
import pyautogui as p
import math
mouse = Controller()
cap = cv2.VideoCapture(0)
#heigt and width
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2400)  # set the width of the frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)  # set the height of the frame
##
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1 ,min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


def dist(x, y, x1, y1):
    dis = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (1 / 2)
    return dis


def action(ac1, ac2):
    if l4_17 < ac1:
        cv2.circle(img, (cx2, cy2), 15, (0, 255, 0), cv2.FILLED)
        mouse.click(Button.left, 1)
        print("clc")
        time.sleep(0.6)

    if l17_20 < ac2:
        cv2.circle(img, (cx3, cy3), 15, (0, 255, 0), cv2.FILLED)
        mouse.click(Button.right)
        p.sleep(1.5)
        # cv2.circle(img, (cx2, cy2), 15, (0, 255, 0), cv2.FILLED)
        # mouse.press(Button.left)


while True:
    success, img =cap.read(0)
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                #cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id,cx,cy)
                if id == 8:
                    #print(id, cx, cy)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy),15, (255, 0, 255), cv2.FILLED)

                if id ==  17:
                    #print(id, cx, cy)
                    cx1, cy1 = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx1, cy1),15, (255, 0, 255), cv2.FILLED)

                if id ==  4:
                    #print(id, cx, cy)
                    cx2, cy2 = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx2, cy2),15, (255, 0, 0), cv2.FILLED)

                if id ==  20:
                    #print(id, cx, cy)
                    cx3, cy3 = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx3, cy3),15, (255, 0, 0), cv2.FILLED)

                if id ==  5:
                    #print(id, cx, cy)
                    cx4, cy4 = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx4, cy4),15, (255, 0, 0), cv2.FILLED)






            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)

            #print(cx, cy)
            #cx0 = 3 * (cx - 150)
            #cy0 = 5 * (cy - 200)
            ###acurate:
            #cx0 = cx*(1919/1285)
            #cy0 = cy*(1079/780)
            ###Big:
            cx0 = (cx*((1919+2500)/1285))-900
            cy0 = (cy*((1079+1800)/780))-300

            mouse.position = (cx0, cy0)
            #print(cx,cy)
            ##print(p.position())
            #a1,b1 = cx,cy
            #a2,b2 = cx1,cy1
            #a3,b3 = cx2,cy2
            #print(a1,b1)
            #print(a2,b2)
            #l8_4 = ((b3 - b1) ** 2 + (a3 - a1) ** 2) ** (1 / 2)
            #l4_17 = ((b3 - b2) ** 2 + (a3 - a2) ** 2) ** (1 / 2)

            l8_4 = dist(cx,cy,cx2,cy2)
            l4_17 = dist(cx1,cy1,cx2,cy2)
            l17_20 = dist(cx1,cy1,cx3,cy3)

## ac1 = 70 , ac2 = 60

            #if l8_4 > 40:
                #mouse.release(Button.left)
                #print("j")
                #time.sleep(2)
            ##########
            ####for hand distance from screen ##########
            #l5_17
            l5_17 = dist(cx1, cy1, cx4, cy4)
            hdist = (30/l5_17)*180
            #print(l5_17)
            print(hdist , "cm")
            ####for hand distance from screen ##########

            ac1 = (70/hdist)*80
            ac2 = (60/hdist)*80
            action(ac1,ac2)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 3,(225,0,225),3)

    #cv2.namedWindow("Fullscreen Window",cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    #cv2.setWindowProperty('Fullscreen Window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Fullscreen Window',img)
    cv2.waitKey(1)
    #cv2.destroyAllWindows()