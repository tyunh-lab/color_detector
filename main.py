import cv2

import json
from ditector.ball_ditect import ball
from ditector.goal_ditect import blue, yellow
from ditector.all_ditector import all_ditect

def setup_json(data_to_write = {'status': 'none', 'now_task': 'none'}):
    print(data_to_write)
    with open('data.json', 'w') as f:
        json.dump(data_to_write, f)


def main():
    setup_json()

    setup_json({'status': '', 'now_task': 'ball_ditect'})
    cap = cv2.VideoCapture("video/ball.mp4")
    ball(cap, withGUI=True)

    setup_json({'status': '', 'now_task': 'blue_goal_ditect'})
    cap = cv2.VideoCapture("video/blue_goal.mp4")
    blue(cap, withGUI=True)

    setup_json({'status': '', 'now_task': 'yellow_goal_ditect'})
    cap = cv2.VideoCapture("video/yellow_goal.mp4")
    yellow(cap, withGUI=True)

    cap = cv2.VideoCapture("video/ball_and_goal.mp4")
    all_ditect(cap, withGUI=True)

if __name__ == "__main__":
    main()