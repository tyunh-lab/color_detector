import bluetooth

def send():
    # Bluetoothデバイスのアドレスとポート番号
    bd_addr = "B8:27:EB:BC:96:3C" # 受信側のMACアドレス
    port = 1 # ポート番号

    # Bluetoothソケットを作成
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port)) # 受信側に接続要求を送信

    # データを送信
    data = "Hello, world!"
    sock.send(data)

    # ソケットをクローズ
    sock.close()

def receive():
    # Bluetoothポート番号
    port = 1

    # Bluetoothソケットを作成して接続を待機
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.bind(("", port))
    sock.listen(1)
    client_sock, client_info = sock.accept()
    print("Accepted connection from", client_info)

    # データを受信
    data = client_sock.recv(1024)
    print("Received:", data)

    # ソケットをクローズ
    client_sock.close()
    sock.close() 

if __name__ == "__main__":
    send()