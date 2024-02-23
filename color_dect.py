import cv2 
import requests
import numpy as np


# カメラの読込み
# 内蔵カメラがある場合、下記引数の数字を変更する必要あり
cap = cv2.VideoCapture(0)


while(cap.isOpened()):
    # 1フレーム毎　読込み
    ret, frame = cap.read()

# url = "http://192.168.1.162/capture"


# while True:
    # response = requests.get(url)
    # frame = cv2.imdecode(np.asarray(bytearray(response.content), dtype=np.uint8), 1)
    # # HSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #画像のサイズ
    # frame.shape[0] 縦
    # frame.shape[1] 横

    # オレンジのHSV範囲
    lower_orange = np.array([3, 100, 100])
    upper_orange = np.array([10, 255, 255])

    # 白以外にマスク
    mask_white = cv2.inRange(hsv, lower_orange, upper_orange)
    res_white = cv2.bitwise_and(frame,frame, mask= mask_white)

    # 輪郭抽出
    gray = cv2.cvtColor(res_white, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #　小さいのは省く
    contours = list(filter(lambda x: cv2.contourArea(x) > 300, contours))

    for i in range(len(contours)):
        (x,y), radius = cv2.minEnclosingCircle(contours[i])
        center = (int(x),int(y))
        # ボールの座標
        # print("x: ", f"{x:.2f}", "y: ", f"{y:.2f}", "radius: ", f"{radius:.2f}",)
        
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
# cap.release()
cv2.destroyAllWindows()


# import cv2


# img = cv2.imread('./input.jpg')
# output_img = img.copy()

# img = img[0:540, 0:1920]

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)

# mask_red1 = cv2.inRange(img, (0, 127, 127), (30, 255, 255))
# mask_red2 = cv2.inRange(img, (240, 127, 127), (255, 255, 255))
# img = cv2.bitwise_or(mask_red1, mask_red2)

# circles = cv2.HoughCircles(image=img,
#                            method=cv2.HOUGH_GRADIENT,
#                            dp=1.0,
#                            minDist=100,
#                            param1=100,
#                            param2=10,
#                            minRadius=0,
#                            maxRadius=50)


# for center_x, center_y, radius in circles.squeeze(axis=0).astype(int):
#    cv2.circle(output_img, (center_x, center_y), radius+40, (0, 0, 255), 10)

# cv2.imwrite('./output.jpg', output_img)