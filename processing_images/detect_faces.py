import cv2
import matplotlib.pyplot as plt
from processing_images.loadingImages import loadImages

def detectFace():
    myImages= loadImages() #Load the images and store in "myImages" List
    for im in myImages:
        gray=pre_process(im) #Convert the input image into gray
        im2=loadClassifier(gray, im) #Start processing the input image
        plt.figure(figsize=(20, 10)) #plot a figure and show the output
        plt.imshow(im2)
        plt.waitforbuttonpress()
        plt.axis('off')

def pre_process(img):
    gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray_img

def loadClassifier(gray, img): # to Load a Classifier and start detecting faces
  face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
  face = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
  for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img_rgb

