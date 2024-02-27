import cv2 
import numpy as np


# カメラの読込み
# 内蔵カメラがある場合、下記引数の数字を変更する必要あり
# cap = cv2.VideoCapture(0)

# 動画の読込み
cap = cv2.VideoCapture("IMG_5908.mp4")

while (cap.isOpened()):
    # 1フレーム毎　読込み
    ret, frame = cap.read()
    # フレームがない場合、終了
    if (frame is None):
        break
    # 画像をHSVに変換
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # オレンジ色のHSV範囲を指定
    # lower_orange = np.array([30, 80, 80])  # 下限値
    # upper_orange = np.array([45, 255, 255])  # 上限値
    lower_orange = np.array([0, 0, 0])  # 下限値
    upper_orange = np.array([255, 255, 255])  # 上限値

    # 指定した範囲内のピクセルを抽出
    orange_mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

    res_orange = cv2.bitwise_and(frame,frame, mask= orange_mask)

    # 輪郭抽出
    gray = cv2.cvtColor(res_orange, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #　小さいのは省く
    contours = list(filter(lambda x: cv2.contourArea(x) > 300, contours))

    for i in range(len(contours)):
        (x,y), radius = cv2.minEnclosingCircle(contours[i])
        center = (int(x),int(y))
        # ボールの座標
        # print("x: ", f"{x:.2f}", "y: ", f"{y:.2f}", "radius: ", f"{radius:.2f}",)

        # 円の中のは省く
        if cv2.pointPolygonTest(contours[i], center, True) > -1:
            continue
        
        # 中心からのx,yの距離
        print("x: ", f"{(x - frame.shape[1]/2):.2f}", "y: ", f"{(y - frame.shape[0]/2):.2f}", "radius: ", f"{radius:.2f}",)

        # ボールの中心を表示
        frame = cv2.circle(frame,center,5,(0,0,255),-1)

        # 画像の中心とボールの中心を結ぶ線を表示
        frame = cv2.line(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)), (int(x),int(y)), (255,0,0), 2)

        # 角度を表示
        angle = np.arctan2(y - frame.shape[0]/2, x - frame.shape[1]/2) * 180 / np.pi
        frame = cv2.putText(frame, f"{angle:.2f}", (int(x),int(y)), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2, cv2.LINE_4)
        #大きさを表示
        frame = cv2.putText(frame, f"{radius:.2f}", (int(x),int(y) + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2, cv2.LINE_4)

        # ボールの円を表示
        radius = int(radius)
        frame = cv2.circle(frame,center,radius,(0,255,0),2)

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