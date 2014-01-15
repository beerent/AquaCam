# Crafter: Brent Ryczak
# Dependencies: opencv

# cam.py is a program in python to use the designated camera to
# take and save photos.

import cv

cv.NamedWindow("Brent's AquaCam!", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

def getPicture():
    img = cv.QueryFrame(capture)
    cv.ShowImage("Brent's AquaCam!", img)
    cv.SaveImage("test.jpg", img)

def displayVideo():
    frame = cv.QueryFrame(capture)
    cv.ShowImage("Brent's AquaCam", frame)
    c = cv.WaitKey(10)

getPicture()
