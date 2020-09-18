# Video-Collage-Maker
Simple script to get images from video and create a singular collage/montage image.
Does this by getting an interger value command line argument then splitting the video equally by that amount.
e.g. A video is 10 minutes long and a split argument of 2 is put in. Then it would get an image from minute 0 and minute 5, then combine into one image.

Done using opencv.

| Arguments  | Purpose |
| ------------- | ------------- |
| -v  | Path of video  |
| -s  |  Number of images to get from video for collage |
| -n | Name of collage/montage image |
| -r | Number of rows in collage |
| -c | Number of columns in collage |
