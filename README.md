# Object_Detection

This script implements real-time object detection using YOLO models and your webcam. It captures video frames, processes them through a trained YOLO model, and displays the detected objects with bounding boxes and confidence scores. The output video is saved in AVI format for later review.

## Acknowledgments

This code is an improvement based on the codebase from [Dipankar Medhi](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993)

## Features
* Real-time Object Detection: Process video frames on-the-fly using YOLO models.
* Customizable Model and Output: Specify your YOLO model file and output video path via command-line arguments.
* User-friendly Interface: Displays detected objects in real-time on the video feed.

## Requirements
1. Python 3.x and pip installed
2. An objection detection model like YOLOv10
3. A webcam

## Installation

1. Clone the repository with the following command:
```
git clone https://github.com/KPCOFGS/Object_Detection.git
cd Object_Detection
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Install [YOLOv10](https://docs.ultralytics.com/models/yolov10/#how-can-i-get-started-with-running-inference-using-yolov10) model

## Usage

To run the script, use the following command:
```
python main.py <model_path> --output <output_path>
```
model_path: Path to your YOLO model file (must end with .pt).

--output: (Optional) Path to save the output video (default is output.avi, must end with .avi).

## Example Usage
```
python main.py yolov10x.pt --output detected_objects.avi
```
To exit the script, use Ctrl + C in the terminal that runs the script. This will terminate the script gracefully

## License

This repository is licensed under the Unlicense, see the [LICENSE](LICENSE) file for more details
