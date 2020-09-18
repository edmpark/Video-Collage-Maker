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
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-s", "--split", type=int, default="4",
	help="number of images to get from video for collage")
ap.add_argument("-n", "--name", type=str, default="montage",
	help="name of collage/montage")
ap.add_argument("-r", "--row", type=int, required=False,
	help="number of row in collage")
ap.add_argument("-c", "--col", type=int, required=False,
	help="number of column in collage")
args = vars(ap.parse_args())

# Read the video from specified path
cam = cv2.VideoCapture(args["video"])

if not cam.isOpened(): 
    print ("could not open :")
    quit()

# number of times to screenshot video in equal proportion of video length
split = args["split"]

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
length = round(int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) / split)

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

#------combining image part------
# grab the paths to the images
imagePaths = list(paths.list_images(args["images"]))
images = []

# loop over the list of image paths
for imagePath in imagePaths:
	# load the image and update the list of images
	image = cv2.imread(imagePath)
	images.append(image)

# construct the montages for the images
montages = build_montages(images, (196, 128), (args["col"], args["row"]))
for montage in montages:
	cv2.imwrite("Montage.jpg", montage)
	cv2.waitKey(0)

#removes all individual collage images in image directory
files = glob.glob(args["images"]+"/*")
for f in files:
    os.remove(f)

