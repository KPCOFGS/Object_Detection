import argparse
import os
from ultralytics import YOLO
import cv2

# Set up argparse to get the model path and output video path from the user
parser = argparse.ArgumentParser(description='YOLO Object Detection')
parser.add_argument('model_path', type=str, help='Path to the YOLO model file (should end with .pt)')
parser.add_argument('--output', type=str, default='output.avi', help='Path to save the output video (should end with .avi)')
args = parser.parse_args()

# Check if the model path ends with .pt
if not args.model_path.endswith('.pt'):
    print("Error: Model path must end with .pt")
    exit()

# Check if the output path ends with .avi
if not args.output.endswith('.avi'):
    print("Error: Output path must end with .avi")
    exit()

# Load the video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Load the YOLO model
model = YOLO(args.model_path)

# Get video frame width, height and define the codec
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use XVID codec
out = cv2.VideoWriter(args.output, fourcc, 20.0, (frame_width, frame_height))

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture image")
            break

        results = model(img)

        # coordinates
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cls = int(box.cls[0])
                confidence = box.conf[0]
                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (0, 255, 0)
                thickness = 2
                cv2.putText(img, f"{r.names[cls]}: {confidence:.2f}", org, font, fontScale, color, thickness)

        # Write the frame to the video file
        out.write(img)

        # Show the output frame
        cv2.imshow('Output', img)
        cv2.waitKey(1)

except KeyboardInterrupt:
    print("Keyboard interrupt received, exiting...")
cap.release()
out.release()  # Release the VideoWriter
cv2.destroyAllWindows()
