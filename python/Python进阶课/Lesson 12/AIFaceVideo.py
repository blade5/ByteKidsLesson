import face_recognition
import cv2

# Open the input movie file
input_movie = cv2.VideoCapture("videos/video.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('output.avi', fourcc, 30, (544, 960))

# Initialize some variables
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Label the results
    for face_location in face_locations:
        top, right, bottom, left = face_location
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (22, 217, 75), 2)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

    frame_number += 1

# All done!
input_movie.release()
cv2.destroyAllWindows()
