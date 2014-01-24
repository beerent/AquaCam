# Crafter: Brent Ryczak
# Dependencies: opencv 2.4.8

# cam.py is a program in python to use the designated camera to
# take and save photos.

import cv

cv.NamedWindow("Brent's AquaCam!", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

def getPicture():
    imgName = "test.jpg"
    img = cv.QueryFrame(capture)
    cv.ShowImage("Brent's AquaCam!", img)
    cv.SaveImage(imgName, img)
    print"file saved as", imgName

def displayVideo():
    x = 1
    while x == 1:
        frame = cv.QueryFrame(capture)
        cv.ShowImage("Brent's AquaCam", frame)
        c = cv.WaitKey(10) 

def runServer():
    import socket

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 5678))
    serversocket.listen(5)
    print 'waiting...'
    
    conn, addr = serversocket.accept()
    print "connection made by", addr
    #read from client...
    data = "brent" 
    data = data, conn.recv(1024)
    print "in: ", data

def printOptions():
    input = raw_input("1) run server\n2) take photo\n3) display video: ")
    input = int(input)
    if (input == 1): 
        runServer()
    elif(input == 2): 
        getPicture()
    elif(input == 3): 
        displayVideo()
    else: 
        print input == 1
def main():
    print("Welcome to AquariCam\n")
    printOptions()

main()
