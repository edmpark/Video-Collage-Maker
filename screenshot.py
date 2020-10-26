# Importing all necessary libraries
from imutils import build_montages
from imutils import paths
import argparse
import cv2
import os
import glob
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required= True,
    help="path of video")
ap.add_argument("-i", "--images", default="data",
	help="path to input directory of images")
ap.add_argument("-s", "--split", type=int, default="4",
	help="number of images to get from video for collage")
ap.add_argument("-n", "--name", type=str, default="montage",
	help="name of collage/montage")
ap.add_argument("-r", "--row", type=int, required=False,
	help="number of row in collage")
ap.add_argument("-c", "--col", type=int, required=False,
	help="number of column in collage")
ap.add_argument("-a", "--auto", action='store_true',
	help="# of splits = row x col")
args = vars(ap.parse_args())

# Read the video from specified path
cam = cv2.VideoCapture(args["video"])

if not cam.isOpened(): 
    print ("could not open :")
    quit()
try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# current frame # in loop
currentframe = 0

# number of times to screenshot video in equal proportion of video length
if args["auto"]:
    split = args["row"] * args["col"]
else:
    split = args["split"]

# gets # of frames of a split video segment 
length = round(int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) / split)

#keeps track of how many screenshots were taken from video so far in loop
image_count = 0

#images array which will then all be combined after while loop
images = []

while (True): 
    # reading from frame
    ret, frame = cam.read()
    if ret:
        if image_count < split:  
            image_count += 1
            name = './data/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frame)
            images.append( cv2.imread(name) )
            currentframe += length
            cam.set(1, currentframe)
        #print(currentframe)
    else:
      print("Done")
      break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

# construct the montages for the images
montages = build_montages(images, (196, 128), (args["col"], args["row"]))
for montage in montages:
	cv2.imwrite("Montage.jpg", montage)
	cv2.waitKey(0)

#removes all individual collage images in image directory
files = glob.glob(args["images"]+"/*")
for f in files:
   os.remove(f)

