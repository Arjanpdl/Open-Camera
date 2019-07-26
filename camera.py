import cv2,time

#open camera
video = cv2.VideoCapture(0)

while True:
    a= 0
    check, frame = video.read()
    #prints all frame rate of object
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing",frame)
    
    key=cv2.waitKey(1)
    if key == ord('q'):
        break


print(a)
# trun off camera
video.release()