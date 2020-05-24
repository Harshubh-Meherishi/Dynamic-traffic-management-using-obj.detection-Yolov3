import cv2
import os
vidcap = cv2.VideoCapture('videos/traffic1.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = vidcap.read()
    #print('read a new frame:',success)
    if count%(10*fps) == 0 :
         cv2.imwrite('output/frames/frame%d.jpg'%count,image)
         os.system('python3 yolo.py --image output/frames/frame%d.jpg --yolo yolo-coco'%count)
         print('successfully written 5th frame')
    count+=1
 
os.system('python3 video_convert.py')
