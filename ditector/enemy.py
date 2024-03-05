#TODO: blue_goal_ditect, yellow_goal_ditectのコストが大きいのでいずれかは内包させる
# もしかしたら機体の向きを取得し、ゴールからの延長線上に敵がいない（ゴールが検出されている）状態ならシュートする方針に変える可能性あり

import cv2
import numpy as np

from .goal_ditect import blue_goal_ditect, yellow_goal_ditect

def enemy_ditect(frame, hsv_image):
    b_x, b_y, b_w, b_h = 0.1, 0.1, 0.1, 0.1
    y_x, y_y, y_w, y_h = 0.1, 0.1, 0.1, 0.1

    blue_goal_contours = blue_goal_ditect(frame, hsv_image)
    yellow_goal_contours = yellow_goal_ditect(frame, hsv_image)

    #青色ゴールのx,y,w,hを取得
    if(len(yellow_goal_contours) != 0):
        for i in range(len(blue_goal_contours)):
            b_x, b_y, b_w, b_h = cv2.boundingRect(blue_goal_contours[i])

    #黄色ゴールのx,y,w,hを取得
    if(len(yellow_goal_contours) != 0):
        for i in range(len(yellow_goal_contours)):
            y_x, y_y, y_w, y_h = cv2.boundingRect(yellow_goal_contours[i])


    # 自陣のゴールによって分ける必要があり
    # 2つ以上のcontourがある場合は敵がいると判断
    # また、アスペクト比が4以下も敵がいると判断
    if(len(blue_goal_contours) > 2):
        print("enemy is detected")
    elif(b_w/b_h <= 4):
        print("enemy is detected")
    else:
        print("goal is open")

    if(len(yellow_goal_contours) > 2):
        print("enemy is detected")
    elif(y_w/y_h <= 4):
        print("enemy is detected")
    else:
        print("goal is open")
