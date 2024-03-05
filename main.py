import cv2

import json
from ditector.ball_ditect import ball
from ditector.goal_ditect import blue, yellow
from ditector.all_ditector import all_ditect
from ditector.line_ditector import line
# from ditector.enemy import enemy

def setup_json(data_to_write = {'status': 'none', 'now_task': 'none'}):
    print(data_to_write)
    with open('data.json', 'w') as f:
        json.dump(data_to_write, f)

def main():
    print('\033[32m'+'setup json start...'+'\033[0m')
    setup_json()

    # cap = cv2.VideoCapture("video/ball_and_goal.mp4")
    # line(cap, withGUI=True) 
    # cap = cv2.VideoCapture("video/blue_goal.mp4")
    # line(cap, withGUI=True)
    # cap = cv2.VideoCapture("video/yellow_goal.mp4")
    # line(cap, withGUI=True)

    # setup_json({'status': '', 'now_task': 'ball_ditect'})
    # cap = cv2.VideoCapture("video/ball.mp4")
    # ball(cap, withGUI=True)

    # setup_json({'status': '', 'now_task': 'blue_goal_ditect'})
    # cap = cv2.VideoCapture("video/blue_goal.mp4")
    # blue(cap, withGUI=True)

    # setup_json({'status': '', 'now_task': 'yellow_goal_ditect'})
    # cap = cv2.VideoCapture("video/yellow_goal.mp4")
    # yellow(cap, withGUI=True)

    # cap = cv2.VideoCapture("video/enemy.mp4")
    # enemy(cap, withGUI=True)

    # cap = cv2.VideoCapture("video/ball_and_goal.mp4")
    cap = cv2.VideoCapture("video/enemy.mp4")
    blue(cap, withGUI=True)
    # all_ditect(cap,withGUI=True)

if __name__ == "__main__":
    main()

#TODO:自陣のゴールがどちらか知っておく必要がある


# import bluetooth

# def send():
    # Bluetoothデバイスのアドレスとポート番号
    # bd_addr = "B8:27:EB:BC:96:3C" # 受信側のMACアドレス
    # port = 1 # ポート番号

    # # Bluetoothソケットを作成
    # sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # sock.connect((bd_addr, port)) # 受信側に接続要求を送信

    # # データを送信
    # data = "Hello, world!"
    # sock.send(data)

    # # ソケットをクローズ
    # sock.close()

# def receive():
#     # Bluetoothポート番号
#     port = 1

#     # Bluetoothソケットを作成して接続を待機
#     sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     sock.bind(("", port))
#     sock.listen(1)
#     client_sock, client_info = sock.accept()
#     print("Accepted connection from", client_info)

#     # データを受信
#     data = client_sock.recv(1024)
#     print("Received:", data)

#     # ソケットをクローズ
#     client_sock.close()
#     sock.close() 

# if __name__ == "__main__":
#     send()