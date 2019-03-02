import cv2
import boto3
# import imutils

width=480
# camera = cv2.VideoCapture("rtsp://admin:ez4me2no@192.168.1.10:554/11")
# camera = cv2.VideoCapture("https://s3.amazonaws.com/alexatestechonewsroom/512.png")
# camera = cv2.VideoCapture('https://s.yimg.com/cv/apiv2/default/20180706/360_video.mp4')

index=0
while True:
    camera = cv2.VideoCapture("rtsp://admin:ez4me2no@192.168.1.10:554/11")
    (grabbed, frame) = camera.read()
    if not grabbed:
        break

    # frame = imutils.resize(frame, width=width)
    retval, buffer = cv2.imencode('.jpg', frame)
    bytes = buffer.tobytes()

    s3 = boto3.resource('s3')
    # s3 = boto3.client('s3')
    index += 1
    print(index)
    # Upload a new file
    s3.Bucket('ipcam-parkinglot').put_object(Key='ipcam.jpg',
        Body=bytes, ContentEncoding='base64',
        ContentType='image/jpg', ACL='public-read')

    s3.Bucket('ipcam-parkinglot').put_object(Key=str(index) + '.jpg',
        Body=bytes, ContentEncoding='base64',
        ContentType='image/jpg', ACL='public-read')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow("Parkinglot Feed", frame)

camera.release()
cv2.destroyAllWindows()
