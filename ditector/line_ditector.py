import cv2 
import numpy as np

def line_ditect(frame,hsv_image):
    # 白のHSV範囲を指定
    lower_white = np.array([0, 0, 200])  # 下限値
    upper_white = np.array([180, 20, 255])  # 上限値

    # 指定した範囲内のピクセルを抽出
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)
    res_white = cv2.bitwise_and(frame,frame, mask= white_mask)

    # 輪郭抽出
    gray = cv2.cvtColor(res_white, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


####デバッグ用#####
def line(cap, withGUI=False):
    while (cap.isOpened()):
    # 1フレーム毎　読込み
        ret, frame = cap.read()

        # フレームがない場合終了
        if (frame is None):
            break

        # ブラー処理
        blured_frame = cv2.GaussianBlur(frame, (33, 33), 0) # <-奇数にしないといけないらしい

        # 画像をHSVに変換
        hsv_image = cv2.cvtColor(blured_frame, cv2.COLOR_BGR2HSV)

        # 白のHSV範囲を指定
        lower_white = np.array([0, 0, 200])  # 下限値
        upper_white = np.array([180, 30, 255])  # 上限値

        # 指定した範囲内のピクセルを抽出
        white_mask = cv2.inRange(hsv_image, lower_white, upper_white)
        res_white = cv2.bitwise_and(frame,frame, mask= white_mask)

        # 輪郭抽出
        gray = cv2.cvtColor(res_white, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if withGUI:
            # 点を表示
            frame = cv2.drawContours(frame, contours, -1, (0,255,0), 3)

            # GUIに表示
            cv2.imshow("Camera", frame)
            #マスク画像を表示
            # cv2.imshow("Mask", white_mask)

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
