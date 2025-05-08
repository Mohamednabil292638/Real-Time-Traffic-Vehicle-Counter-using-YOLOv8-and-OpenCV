## 🚦 Real-Time Traffic Vehicle Counter using YOLOv8 and OpenCV

This project implements a real-time traffic monitoring system that detects, tracks, and counts vehicles from video footage — like a smart traffic police system powered by AI. It uses **YOLOv8** for object detection and **DeepSORT** for multi-object tracking.

## 📝 Description

The system assigns unique IDs to detected vehicles, tracks their movement across frames, and counts them as they cross a virtual line. This is useful for analyzing traffic flow, vehicle congestion, or creating intelligent traffic solutions.

All detection, tracking, and counting are done in real-time using open-source Python libraries.

## 🚀 Features

- 🚗 Vehicle detection using YOLOv8
- 🆔 Vehicle tracking with DeepSORT
- 🔢 Live counting of vehicles crossing a virtual line
- 🖥️ Real-time processing on recorded or live video
- 🎯 Customizable to specific classes (car, bike, bus, etc.)
- 🎥 Visual output with bounding boxes, track IDs, and counts

## 🛠️ Built With

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- DeepSORT (Simple Online and Realtime Tracking)

## 📹 Demo

🎬 *Demo video showing vehicle detection and counting in action*  
📷 Video footage captured and edited by me.

> (Add video link or GitHub upload here)

## 📁 Project Structure

├── main.py # Main script for detection & tracking
├── tracker.py # DeepSORT tracking logic
├── utils.py # Helper functions
├── input/traffic.mp4 # Sample input video
├── output/result.mp4 # Output with detection & count
├── requirements.txt # Required Python packages
└── README.md # Project documentation

csharp
Copy
Edit

## 🧾 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install ultralytics opencv-python numpy
Make sure to use Python 3.8 or above.

💡 How It Works
Load the YOLOv8 model.

Read frames from a video.

Detect objects (vehicles) in each frame.

Track them using DeepSORT.

Count when tracked vehicles cross a predefined line.

Display results in real-time with bounding boxes and counters.

📌 Use Cases
Traffic monitoring systems

Vehicle flow analysis

Smart surveillance

Real-time AI demos for education

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Mohamed Nabil S
GitHub • LinkedIn
