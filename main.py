import time
import cv2

from ball_ditect import color_ditect
from goal_ditect import blue_goal_ditect, yellow_goal_ditect

def main():
    start = time.time()
    cap = cv2.VideoCapture("video/ball.mp4")
    color_ditect(cap)
    print("time: ", time.time() - start)
    cap = cv2.VideoCapture("video/blue_goal.mp4")
    blue_goal_ditect(cap)
    print("time: ", time.time() - start)
    cap = cv2.VideoCapture("video/yellow_goal.mp4")
    yellow_goal_ditect(cap)
    print("time: ", time.time() - start)


if __name__ == "__main__":
    main()