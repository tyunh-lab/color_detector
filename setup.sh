#opencvのインストール
sudo apt install -y libatlas-base-dev
# 依存パッケージのインストール
sudo apt install -y libavutil56 libcairo-gobject2 libgtk-3-0 libqtgui4 libpango-1.0-0 libqtcore4 libavcodec58 libcairo2 libswscale5 libtiff5 libqt4-test libatk1.0-0 libavformat58 libgdk-pixbuf2.0-0 libilmbase23 libjasper1 libopenexr23 libpangocairo-1.0-0 libwebp6
sudo pip3 install opencv-python==4.1.0.25

# pyBluez の依存パッケージをインストール
sudo apt-get install -y python-dev libbluetooth3-dev

# pyBluez のインストール
sudo pip install pybluez

# gattlib の依存パッケージをインストール
sudo apt-get install -y libbluetooth3-dev

# BLEを使う場合に必要な gattlib をインストール
sudo pip install gattlib

# psutil のインストール
pip install psutil 

# firebaseのインストール
pip3 install --upgrade firebase-admin

# serialのインストール
pip3 install pyserial