import cv2
from picamera2 import Picamera2
# from picamera2 import controls
from libcamera import controls
import numpy as np
from ditector.ball_ditect import ball_ditect
from ditector.goal_ditect import blue_goal_ditect, yellow_goal_ditect

import math

from util.uart import uart, writewords

def all_ditect(withGUI=False, withSaveVideo=False):
    # picameraの設定
    camera = PiCamera2()
    camera.configure(camera.create_preview_configuration(main={"format":'XRGB8888',"size":(1920,1920)}))
    camera.start()
    camera.set_controls({'AfMode': controls.AfModeEnum.Continuous})
    # 画像を取得
    image = camera.capture_array()
    #画像が3次元配列でない場合、3次元配列に変換
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    if channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if channels == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    frame = image

    # 動画の保存
    if withSaveVideo:
        # 動画の保存設定mp4
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        fps = 30
        frame_width = int(frame.shape[1])
        frame_height = int(frame.shape[0])
        out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))
    
    while (True):
        # 1フレーム毎　読込み
        frame = camera.capture_array()
        # 画像が3次元配列でない場合、3次元配列に変換
        channels = 1 if len(frame.shape) == 2 else frame.shape[2]
        if channels == 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        if channels == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # フレームがない場合終了
        if (frame is None):
            break

        # ブラー処理
        blured_frame = cv2.GaussianBlur(frame, (111, 111), 0) # <-奇数にしないといけない、値を大きくすると重くなる

        # 画像をHSVに変換
        hsv_image = cv2.cvtColor(blured_frame, cv2.COLOR_BGR2HSV)

        # ボールの検出
        ball_contours = ball_ditect(blured_frame,hsv_image)
        blue_goal_contours = blue_goal_ditect(blured_frame,hsv_image)
        yellow_goal_contours = yellow_goal_ditect(blured_frame,hsv_image)

        #小さいのはノイズとして削除
        ball_contours = [cnt for cnt in ball_contours if cv2.contourArea(cnt) > 300]
        blue_goal_contours = [cnt for cnt in blue_goal_contours if cv2.contourArea(cnt) > 1000]
        yellow_goal_contours = [cnt for cnt in yellow_goal_contours if cv2.contourArea(cnt) > 1000]
        
        #for debug
        # enemy_ditect(frame, hsv_image)
        
        # ボールの検出
        for i in range(len(ball_contours)):
            (x,y), radius = cv2.minEnclosingCircle(ball_contours[i])
            center = (int(x),int(y))
            ball_angle = math.atan2(x - frame.shape[1]/2, y - frame.shape[0]/2) * 180 / math.pi
            writewords(f'{ball_angle},{radius}')

            if withGUI or withSaveVideo:
                # ボールの中心を表示
                frame = cv2.circle(frame,center,5,(0,0,255),-1)
                # 中心から線を表示
                frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), center, (255,0,0), 2)
                # 角度を表示
                frame = cv2.putText(frame, f"{(x - frame.shape[1]/2):.2f}", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # 大きさを表示
                frame = cv2.putText(frame, f"{radius:.2f}", (int(x),int(y) + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # ボールの円を表示
                frame = cv2.circle(frame,center,int(radius),(0,0,255),2)
        
        # ゴールの検出
        for i in range(len(blue_goal_contours)):
            #旧バージョン
            # x,y,w,h = cv2.boundingRect(blue_goal_contours[i])
            # center = (int(x + w/2), int(y + h/2))
            # aspect_ratio = w/h
            #改良版
            rect = cv2.minAreaRect(blue_goal_contours[i])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            center = (int(rect[0][0]), int(rect[0][1]))
            aspect_ratio = rect[1][0]/rect[1][1]
            x = rect[0][0]
            y = rect[0][1]

            if withGUI or withSaveVideo:
                # ゴールの枠を表示
                # frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.drawContours(frame,[box],0,(0,255,0),2)
                # アスペクト比を表示
                frame = cv2.putText(frame, f"{aspect_ratio:.2f}", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                # ゴールの中心を表示
                frame = cv2.circle(frame,center,5,(0,0,255),-1)
                # 中心から線を表示
                frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), center, (255,0,0), 2)
        
        # ゴールの検出
        for i in range(len(yellow_goal_contours)):
            #旧バージョン
            # x,y,w,h = cv2.boundingRect(yellow_goal_contours[i])
            # center = (int(x + w/2), int(y + h/2))
            # aspect_ratio = w/h
            #改良版
            rect = cv2.minAreaRect(yellow_goal_contours[i])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            center = (int(rect[0][0]), int(rect[0][1]))
            aspect_ratio = rect[1][0]/rect[1][1]
            x = rect[0][0]
            y = rect[0][1]

            if withGUI or withSaveVideo:
                # ゴールの枠を表示
                # frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.drawContours(frame,[box],0,(0,255,0),2)
                # アスペクト比を表示
                frame = cv2.putText(frame, f"{aspect_ratio:.2f}", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                # ゴールの中心を表示
                frame = cv2.circle(frame,center,5,(0,0,255),-1)
                # 中心から線を表示
                frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), center, (255,0,0), 2)
        
        if withGUI:
            # 画像の中心を表示
            frame = cv2.circle(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)),5,(0,0,255),-1)
            # GUIに表示
            cv2.imshow("Camera", frame)
        
        if withSaveVideo:
            # 動画の保存
            out.write(frame)
        
        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # print("elapsed_time:{0}".format(time.time() - start) + "[sec]")
    # print("frame_length:{0}".format(frame_length))
    # print("fps:{0}".format(frame_length / (time.time() - start)))
        
    if withSaveVideo:
        out.release()
        # pushVido()
    
    # 終了処理
    cv2.destroyAllWindows()