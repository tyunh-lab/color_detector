import cv2
import threading

from ditector.ball_ditect import ball
from ditector.goal_ditect import blue, yellow
from ditector.all_ditector import all_ditect
from ditector.line_ditector import line

import os

from util.json_manager import setup_json, write_json_overwrite

import logger

dir_path = "video"

def main():
    video_paths = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    for video_path in video_paths:
        write_json_overwrite({'status': 'now', 'now_task': 'all_ditect', 'video_path': f'{video_path}'})
        cap = cv2.VideoCapture(f'{dir_path}/{video_path}')
        all_ditect(cap)
    write_json_overwrite({'status': 'done', 'now_task': 'none'})

if __name__ == "__main__":
    setup_json()
    thread1 = threading.Thread(target=logger.logger)
    thread1.start()
    # thread1.join() #<-終わるまで次に進まない
    main()

#TODO:自陣のゴールがどちらか知っておく必要がある