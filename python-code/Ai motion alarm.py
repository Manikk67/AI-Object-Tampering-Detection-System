import cv2
import time
import imutils
import serial

#arduino connection
arduino = serial.Serial('COM5', 9600)

time.sleep(5)

#camera start
cam = cv2.VideoCapture(0)

time.sleep(2)

firstFrame = None

#large object detection area
area = 15000

while True:

    _, img = cam.read()

    text = "Normal"

    #resize image
    img = imutils.resize(img, width=1000)

    #convert to gray
    grayImg = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    #smooth image
    gaussianImg = cv2.GaussianBlur(
        grayImg,
        (31, 31),
        0
    )

    #capture first frame
    if firstFrame is None:

        firstFrame = gaussianImg

        continue

    #difference between first frame and current frame
    imgDiff = cv2.absdiff(
        firstFrame,
        gaussianImg
    )

    #threshold
    threshImg = cv2.threshold(
        imgDiff,
        50,
        255,
        cv2.THRESH_BINARY
    )[1]

    #dilation
    threshImg = cv2.dilate(
        threshImg,
        None,
        iterations=4
    )

    #find contours
    cnts = cv2.findContours(
        threshImg.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    cnts = imutils.grab_contours(cnts)

    tamperDetected = False

    for c in cnts:

        #ignore small changes
        if cv2.contourArea(c) < area:

            continue

        tamperDetected = True

        (x, y, w, h) = cv2.boundingRect(c)

        #draw rectangle
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    #if object removed / scene changed
    if tamperDetected == True:

        text = "OBJECT TAMPER DETECTED"

        arduino.write(b'1')

        print("ALARM")

    else:

        text = "Normal"

        arduino.write(b'0')

    #display text
    cv2.putText(
        img,
        text,
        (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    #show camera
    cv2.imshow(
        "cameraFeed",
        img
    )

    #press q to quit
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):

        break

#release camera
cam.release()

#close windows
cv2.destroyAllWindows()
