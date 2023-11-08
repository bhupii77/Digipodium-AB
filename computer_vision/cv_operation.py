import cv2
import numpy as np
import os
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"🤯 video file not found\n{path_of_video}")
        return None
    video = cv2.VideoCapture(path_of_video)
    cv2.namedWindow("video")
    cv2.createTrackbar("ksize","video",3,100,lambda x:None)
    
    while True:
        status , frame = video.read()
        height , width , _ = frame.shape
        print()
        if not status:
            print("🤯 video could not be read!!")
            break
        #operations
        #1 resize
        frame = cv2.resize(frame,(None,None),fx = .5,fy=.5)  #none none = n0 particular size

        #2 . convert to grayscale

        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #3.blur 
        ksize= cv2.getTrackbarPos("ksize","video")
        try: frame = cv2.GaussianBlur(frame,(ksize,ksize),0)
        except : pass

        #4. add text

        frame = cv2.putText(
            frame,
            "Uncharted 4 : the lost legacy",
            (width//2,height//2), 
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,225), #RED COLOR
            2 #THICKNESS

        )

        cv2.imshow("video", frame)
        if cv2.waitKey(30) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__=="__main__" :
    videofile = r"E:\edited videos\lv_0_20220526221055.mp4" 
    load_video (videofile)     