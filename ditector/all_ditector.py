import cv2
import numpy as np
from ditector.ball_ditect import ball_ditect
from ditector.goal_ditect import blue_goal_ditect, yellow_goal_ditect

def all_ditect(cap, withGUI=False):
    while (cap.isOpened()):
    # 1フレーム毎　読込み
        ret, frame = cap.read()

        # フレームがない場合終了
        if (frame is None):
            break

        # ブラー処理
        frame = cv2.GaussianBlur(frame, (43, 43), 0) # <-奇数にしないといけない、値を大きくすると重くなる

        # 画像をHSVに変換
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # ボールの検出
        ball_contours = ball_ditect(frame,hsv_image)
        blue_goal_contours = blue_goal_ditect(frame,hsv_image)
        yellow_goal_contours = yellow_goal_ditect(frame,hsv_image)

        #小さいのはノイズとして削除
        ball_contours = [cnt for cnt in ball_contours if cv2.contourArea(cnt) > 300]
        blue_goal_contours = [cnt for cnt in blue_goal_contours if cv2.contourArea(cnt) > 1000]
        yellow_goal_contours = [cnt for cnt in yellow_goal_contours if cv2.contourArea(cnt) > 1000]
        
        # ボールの検出
        for i in range(len(ball_contours)):
            (x,y), radius = cv2.minEnclosingCircle(ball_contours[i])
            center = (int(x),int(y))

            if withGUI:
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
            x,y,w,h = cv2.boundingRect(blue_goal_contours[i])
            center = (int(x + w/2), int(y + h/2))

            if withGUI:
                # ゴールの枠を表示
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # ゴールの中心を表示
                frame = cv2.circle(frame,center,5,(0,0,255),-1)
                # 中心から線を表示
                frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), center, (255,0,0), 2)
        
        # ゴールの検出
        for i in range(len(yellow_goal_contours)):
            x,y,w,h = cv2.boundingRect(yellow_goal_contours[i])
            center = (int(x + w/2), int(y + h/2))

            if withGUI:
                # ゴールの枠を表示
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # ゴールの中心を表示
                frame = cv2.circle(frame,center,5,(0,0,255),-1)
                # 中心から線を表示
                frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), center, (255,0,0), 2)
        
        if withGUI:
            # 画像の中心を表示
            frame = cv2.circle(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)),5,(0,0,255),-1)
            # GUIに表示
            cv2.imshow("Camera", frame)
        
        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()