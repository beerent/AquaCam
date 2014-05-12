import cv2
def tester(): 
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)
    retval, im = camera.read()

    temp = im
    print("Taking image...")
    camera_capture = temp
    file = "/home/brent/test.png"
    cv2.imwrite(file, camera_capture)
    del(camera)
    print ("done")
tester()
tester()