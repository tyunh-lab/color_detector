import cv2
import threading

from ditector.all_ditector import all_ditect

# from util.uart import uart

from util.json_manager import setup_json, write_json_overwrite

import logger

dir_path = "video"

def main():
    all_ditect()
    write_json_overwrite({'status': 'done', 'now_task': 'none'})

if __name__ == "__main__":
    setup_json()
    thread1 = threading.Thread(target=logger.logger)
    # thread2 = threading.Thread(target=uart)
    thread1.start()
    # thread2.start()
    # thread1.join() #<-終わるまで次に進まない
    main()

#TODO:自陣のゴールがどちらか知っておく必要がある