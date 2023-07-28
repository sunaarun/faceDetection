import cv2
import glob
imdir = 'images/' # Directory where the images are located ... or Directory Path
ext = ['png', 'jpg', 'gif','jpeg']  # List of image file extensions to consider

def loadImages(): # our method to load the images from specific path
   # Add image formats here
  files = []
  [files.extend(glob.glob(imdir + '*.' + e)) for e in ext] #find all files in the 'images/'
   # and store them in the files variable
  images = [cv2.imread(file) for file in files] # reads each image file using the cv2.imread() function from
   # OpenCV and stores the loaded images in a list called images.
  return images # return the list of images