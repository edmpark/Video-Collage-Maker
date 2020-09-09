# Importing all necessary libraries
import cv2
import os
import time

# Read the video from specified path
cam = cv2.VideoCapture("SampleVideo.mp4")

if not cam.isOpened(): 
    print ("could not open :")
    quit()

# number of times to screenshot video in equal proportion of video length
split = 4

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

# gets duration of video
length = round(int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) / (split-1))
print(length)

while (True): 
    # reading from frame
    ret, frame = cam.read()

    if ret:
        if currentframe % length == 0:  
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
        currentframe += 1
    else:
      print("Done")
      break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()