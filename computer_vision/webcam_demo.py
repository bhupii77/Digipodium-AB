import cv2
import numpy as np
import os
def load_video(camera_index):
    if not os.path.exists(camera_index):
        print(f"🤯 vieo file not found\n{camera_index}")
        return None
    video = cv2.VideoCapture(camera_index)
    while True:
        status , frame = video.read()
        if not status:
            print("🤯 camera data not recall")
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(30) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__=="__main__" :
    cam_idx = "http://192.168.18.253:4747/video"
    load_video (cam_idx)