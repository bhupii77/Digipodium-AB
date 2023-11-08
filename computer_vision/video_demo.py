import cv2
import numpy as np
import os
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"🤯 vieo file not found\n{path_of_video}")
        return None
    video = cv2.VideoCapture(path_of_video)
    while True:
        status , frame = video.read()
        if not status:
            print("🤯 video could not be read!!")
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(30) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__=="__main__" :
    videofile = r"E:\edited videos\lv_0_20220526221055.mp4" 
    load_video (videofile)     