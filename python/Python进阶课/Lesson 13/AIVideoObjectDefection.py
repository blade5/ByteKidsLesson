import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

# open webcam
video = cv2.VideoCapture("videos/AI/object_defection.mp4")

if not video.isOpened():
    print("Could not open video")
    exit()

# loop through frames
while video.isOpened():

    # read frame from webcam
    status, frame = video.read()

    if not status:
        break

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')

    print(bbox, label, conf)

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press any key to stop
    cv2.waitKey()

# release resources
video.release()
cv2.destroyAllWindows()
