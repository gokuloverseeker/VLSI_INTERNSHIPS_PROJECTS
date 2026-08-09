import cv2
import tensorflow as tf
import numpy as np
import requests
import time

# --------------------------
# Configuration
# --------------------------
MODEL_PATH = "mobilenet_v2_1.0_224.tflite"
LABEL_URL = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"

# --------------------------
# Load labels
# --------------------------
labels = requests.get(LABEL_URL).text.splitlines()

# --------------------------
# Load TensorFlow Lite model
# --------------------------
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]["shape"]
height = input_shape[1]
width = input_shape[2]

print("Camera starting...")

# --------------------------
# Open Laptop Camera
# --------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror image (optional)
    frame = cv2.flip(frame, 1)

    # Keep original frame
    display = frame.copy()

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize
    img = cv2.resize(rgb, (width, height))

    img = np.array(img)

    # Quantized model
    if input_details[0]["dtype"] == np.uint8:
        input_data = img.astype(np.uint8)
    else:
        input_data = img.astype(np.float32)
        input_data = (input_data / 127.5) - 1

    input_data = np.expand_dims(input_data, axis=0)

    interpreter.set_tensor(input_details[0]["index"], input_data)

    start = time.time()

    interpreter.invoke()

    end = time.time()

    output = interpreter.get_tensor(output_details[0]["index"])[0]

    class_id = np.argmax(output)
    score = output[class_id]

    label = labels[class_id]

    inference_time = (end - start) * 1000

    text = f"{label} : {score:.2f}"

    cv2.putText(
        display,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        display,
        f"{inference_time:.2f} ms",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.imshow("Edge AI Camera", display)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
