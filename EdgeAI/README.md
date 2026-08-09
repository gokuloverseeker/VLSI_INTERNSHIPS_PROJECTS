#Edge AI Real-Time Image Classification using TensorFlow Lite

Recently , I had chance to learn about  the hardware edge inference , for edge device and ai in it .... that why i tried to run a simple image classification model in laptop where i get to know about how the model trained loaded and its constraint like OpenCV uses BGR color format, while PIL expects RGB and other things ... hence i just tried out to experience how things work ... lol 

Below is a AI generated Readme file which you can refer .... lol 

A real-time **Edge AI** application that performs image classification using your **laptop webcam** with a **TensorFlow Lite MobileNetV2** model.

Instead of sending images to a cloud server, this project performs **local inference** directly on your machine, demonstrating the fundamentals of **Edge Computing**, **AI Hardware**, and **VLSI-based AI acceleration**.

📸 Demo

The application captures live video from the laptop camera and displays:

- Live webcam feed
- Predicted object label
- Prediction confidence
- Inference time (milliseconds)

Example:
```
Prediction : laptop
Confidence : 0.97
Inference : 5.8 ms
```
# 📖 Project Overview
Artificial Intelligence models are traditionally executed on cloud servers.
```
Camera
   │
   ▼
Internet
   │
   ▼
Cloud Server
   │
   ▼
Prediction
```
This introduces
- Network latency
- Privacy concerns
- Internet dependency
In **Edge AI**, the model runs locally.
```
Laptop Camera
      │
      ▼
TensorFlow Lite Model
      │
      ▼
Prediction
```
Advantages:
- ⚡ Low latency
- 🔒 Better privacy
- 🌐 No internet required for inference
- 🔋 Lower power consumption
# 🛠 Technologies Used
- Python 3
- TensorFlow Lite
- OpenCV
- NumPy
- Pillow
- Requests
# 📂 Project Structure
```
EdgeAI/
│
├── camera_inference.py
├── mobilenet_v2_1.0_224.tflite
├── ImageNetLabels.txt
├── requirements.txt
├── README.md
└── screenshots/
      └── demo.png
```
# ⚙ Installation
## Clone the repository
```bash
git clone https://github.com/<your-username>/EdgeAI.git

cd EdgeAI
```
---
## Create Virtual Environment
Linux/macOS
```bash
python3 -m venv ai_env
```
Activate

```bash
source ai_env/bin/activate
```

Windows

```bash
python -m venv ai_env

ai_env\Scripts\activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
or
```bash
pip install tensorflow opencv-python numpy pillow requests matplotlib
```
# 📥 Download TensorFlow Lite Model

Download the MobileNetV2 TensorFlow Lite model.

Place it inside the project folder as

```
mobilenet_v2_1.0_224.tflite
```

Also download

```
ImageNetLabels.txt
```

---

# ▶ Run the Project

```bash
python camera_inference.py
```

Press

```
Q
```

to quit.

---

# 🔄 Workflow

```
Laptop Camera
        │
        ▼
Capture Frame
        │
        ▼
Resize (224×224)
        │
        ▼
RGB Conversion
        │
        ▼
TensorFlow Lite Interpreter
        │
        ▼
MobileNetV2
        │
        ▼
Prediction
        │
        ▼
Display Label + Confidence + Inference Time
```

---

# 🧠 How It Works

## Step 1

The webcam captures a frame using OpenCV.

```python
cap.read()
```

---

## Step 2

The frame is resized to

```
224 × 224
```

because MobileNetV2 expects that input size.

---

## Step 3

The image is converted into a NumPy tensor.

```python
np.expand_dims()
```

---

## Step 4

The tensor is passed into the TensorFlow Lite interpreter.

```python
interpreter.set_tensor()
```

---

## Step 5

Inference is executed.

```python
interpreter.invoke()
```

---

## Step 6

The output tensor contains probabilities for approximately 1000 ImageNet classes.

The class with the highest probability is selected using

```python
np.argmax()
```

---

## Step 7

The predicted label is displayed on the webcam feed.

---

# 📊 Sample Output

```
Inference Time : 6.3 ms

Prediction : military uniform

Confidence : 0.81
```

---

# 💡 Why TensorFlow Lite?

TensorFlow Lite is optimized for Edge AI.

Advantages

- Small model size
- Fast inference
- Low memory usage
- Low power consumption
- Optimized for embedded devices

---

# 🧩 Why MobileNetV2?

MobileNetV2 is designed specifically for mobile and embedded devices.

Features

- Lightweight architecture
- High accuracy
- Low latency
- Low computational cost

---

# 📈 Applications

- Smart surveillance
- Industrial automation
- Autonomous robots
- Smart agriculture
- Medical devices
- Edge AI cameras
- Intelligent IoT systems

---

# ⚠ Limitations

This project performs **Image Classification**, not **Object Detection**.

It predicts the most dominant object in the frame.

Example

✔ Laptop

✔ Bottle

✔ Person

✔ Keyboard

It does **not**

- Detect multiple objects
- Draw bounding boxes
- Recognize faces
- Track moving objects

---

# 🚀 Future Improvements

- Object Detection using YOLOv8
- TensorFlow Lite Object Detection
- Face Recognition
- Hand Gesture Recognition
- Pose Estimation
- Real-time FPS Counter
- Raspberry Pi Deployment
- NVIDIA Jetson Deployment
- Coral TPU Acceleration
- Custom TensorFlow Lite Models

---

# 📚 Concepts Demonstrated

- Edge AI
- Embedded AI
- TensorFlow Lite
- Image Classification
- Neural Networks
- MobileNetV2
- Real-Time Inference
- OpenCV
- Computer Vision
- AI Hardware Fundamentals
- VLSI for AI Accelerators

---

# 🎯 Learning Outcomes

After completing this project, you will understand

- Running AI models locally
- TensorFlow Lite inference
- Real-time webcam processing
- OpenCV integration
- Edge Computing fundamentals
- AI Hardware acceleration concepts

---

# 📜 License

This project is intended for educational purposes.

Feel free to fork, modify, and experiment.

---

# 👨‍💻 Author
**GOKUL**
B.Tech Electrical & Electronics Engineering
Interested in

- VLSI Design
- Semiconductor Engineering
- Embedded Systems
- AI Hardware
- Edge Computing
- Computer Vision

---
⭐ If you found this project useful, consider giving it a star! or else I would call Deadpool...lol
