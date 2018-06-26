import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import argparse
from MyKey import MyKey

# use mouse to select origin point
def mouse_callback(event,x,y,flags,param):
    # grab references to the global variables
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDBLCLK:
        refPt = [(x, y)]
        print(refPt)
        
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        print(refPt)
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        if abs(x-refPt[0][0]) > 10 and abs(y-refPt[0][1]) > 10:
            refPt.append((x, y))
            cropping = False
            # draw a rectangle around the region of interest
            cv2.rectangle(resized, refPt[0], refPt[1], (0, 255, 0), 2)
            cv2.imshow("resized", resized)

def reduceReflections(image):
    # reduce reflections in image

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    v = clahe.apply(v)

    hsv = cv2.merge([h, s, v])
    hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    cv2.imshow("reduced reflection", hsv)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return hsv

def applyGaussianBlur(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (7, 7), 0)
    cv2.imshow("gaussian blur", gray_image)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return gray_image

def detectEdges(image):
    edges = cv2.Canny(image,0,200)
    cv2.imshow("edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edges


# load and show file
images_folder_path = os.getcwd() + "\images\\" 

image_path = images_folder_path + "lw5_unocode_525233.jpg"

image = cv2.imread(image_path)
# cv2.imshow("orginal", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
image_shape = image.shape
# print(image.shape)

# scale image down to 1000 pixels
r = 1000.0/image.shape[1]
dim = (1000,int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.namedWindow("resized")
cv2.setMouseCallback("resized", mouse_callback)
clone = resized.copy()

while True:
    cv2.imshow("resized", resized)
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        cv2.destroyAllWindows()
        break
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    show_roi = cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("roi.jpg",roi)
    image = roi
    original = roi

image = reduceReflections(image)
# image = applyGaussianBlur(image)
edge_image = detectEdges(image)





        
    
