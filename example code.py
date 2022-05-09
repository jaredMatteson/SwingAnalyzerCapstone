########################################################################################################################
#
## Author Name: Jared Matteson
#
## Project Name: Swing Analyzer
#
## Date Created: January 01, 2022
#
## Date Updated: May 04, 2022
#
## Class: SENG 4210 Senior Project 2
#
## Version #: 1.2
#
## Summary: This is a basic color mask that will enable the user to seperate the color of the club head of the training
# aid from the background using OpenCV for python. The current color mask is set to read orange color ranges and
# values, however further analysis showed that light blue or purple would have been a better option. To change the color
# mask to the the desired color change the lower limit of the HSV color spectrum to the desired color. To change the
# video being viewed make sure you change the path to the media folder on your computer and then choose your own .mp4
# file for analyzing purposes by altering the filename variable.
#
########################################################################################################################




import cv2


import sys
import numpy as np


path = 'C:\\Users\\jarma\\OneDrive - Dunwoody College of Technology\\Spring 2022 Courses\\Senior Project 2\\Basic Ball Tracking\\Prototype Ball Tracking Python Pycharm\\media\\'
filename = 'NowThisOne.mp4'
object = (path+filename)


cap = cv2.VideoCapture(object)

while 1:
    ret, frame = cap.read()
    # ret will return a true value if the frame exists otherwise False
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # changing the color format from BGr to HSV
    # This will be used to create the mask
    L_limit = np.array([6, 100, 70])  # setting the Orange lower limit
    U_limit = np.array([25, 255, 255])  # setting the Orange upper limit

    o_mask = cv2.inRange(into_hsv, L_limit, U_limit)
    # creating the mask using inRange() function
    # this will produce an image where the color of the objects
    # falling in the range will turn white and rest will be black
    orange = cv2.bitwise_and(frame, frame, mask=o_mask)
    # this will give the color to mask.
    cv2.imshow('Original', frame)  # to display the original frame
    cv2.imshow('Orange Detector', orange)  # to display the blue object output

    if cv2.waitKey(1) == 27:
        break
# this function will be triggered when the ESC key is pressed
# and the while loop will terminate and so will the program
cap.release()

cv2.destroyAllWindows()


