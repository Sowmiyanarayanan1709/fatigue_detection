import cv2

# Initialize video capture
video = cv2.VideoCapture(0)  # Use 0 for the default webcam, or a file path for a video file

# Get the frames per second (FPS)
fps = video.get(cv2.CAP_PROP_FPS)
print("Frames per second:", fps)

# Release the video capture object
video.release()
