# AI-Object-Tampering-Detection-System



AI-Based Smart Object Tampering and Theft Detection System

Overview

This project is an AI-powered smart security and anti-theft monitoring system developed using Python, OpenCV, and Arduino UNO.

The system continuously monitors a protected object using Computer Vision techniques. A reference frame containing the object is captured initially. If the object is removed, tampered with, or if the scene changes significantly, the system detects the change and immediately activates an alarm using LEDs and a buzzer connected to Arduino.

Unlike traditional motion detection systems, this project focuses on object tampering detection, making it more suitable for real-world security applications such as jewelry monitoring, museum object protection, and smart surveillance systems.


---

Features

✅ Real-time object tampering detection
✅ Computer Vision based monitoring
✅ Arduino hardware integration
✅ Red and Green status LEDs
✅ Active buzzer alarm system
✅ Reduced false alarms using contour filtering
✅ Real-time frame processing
✅ Low-cost implementation
✅ Beginner-friendly AI + Embedded Systems project


---

Technologies Used

Technology	Purpose

Python	Main programming language
OpenCV	Computer Vision processing
Arduino UNO	Hardware controller
PySerial	Python-Arduino communication
Imutils	Image resizing utility
Embedded Systems	Alarm integration
Computer Vision	Scene comparison and detection



---

System Architecture

Camera
   ↓
Python OpenCV Program
   ↓
Object Tampering Detection
   ↓
Serial Communication
   ↓
Arduino UNO
   ↓
LED + Buzzer Alarm System


---

Hardware Components

Component	Quantity

Arduino UNO	1
Webcam / Laptop Camera	1
Red LED	1
Green LED	1
220Ω Resistor	2
Active Buzzer	1
Breadboard	1
Jumper Wires	Few
USB Cable	1



---

Circuit Connections

Green LED

Arduino Pin 12 → Green LED (+)

Green LED (-) → 220Ω resistor → GND


Red LED

Arduino Pin 13 → Red LED (+)

Red LED (-) → 220Ω resistor → GND


Active Buzzer

Arduino Pin 8 → Buzzer (+)

Buzzer (-) → GND



---

Working Principle

1. The webcam continuously captures live video.


2. The first frame containing the protected object is stored as the reference frame.


3. Every new frame is converted into grayscale and blurred for noise reduction.


4. The current frame is compared with the reference frame.


5. If the protected object is removed or the scene changes significantly, contours are detected.


6. Small contour areas are ignored to reduce false alarms.


7. Python sends a signal to Arduino through serial communication.


8. Arduino activates:

Red LED

Buzzer alarm


9. During normal condition:

Green LED remains ON


---

Python Libraries Required

Install the required libraries using:

pip install opencv-python imutils pyserial


---

How to Run the Project

Step 1 — Hardware Setup

Connect:

Green LED → Pin 12

Red LED → Pin 13

Buzzer → Pin 8



---

Step 2 — Upload Arduino Code

1. Open Arduino IDE.


2. Select Board → Arduino UNO.


3. Select COM Port.


4. Upload Arduino code.




---

Step 3 — Install Python Libraries

pip install opencv-python imutils pyserial


---

Step 4 — Update COM Port

Inside Python code:

arduino = serial.Serial('COM5', 9600)

Replace:

COM5

with your Arduino COM port.


---

Step 5 — Run Python Program

1. Open Python IDLE.


2. Run the Python program.


3. Place protected object inside camera frame.


4. If the object is removed or tampered with:

Red LED turns ON

Buzzer activates

Alarm message displayed





---

Project Output

Normal State

Green LED ON

Red LED OFF

Buzzer OFF


Tampering Detected

Green LED OFF

Red LED ON

Buzzer ON

Bounding rectangle displayed

Alarm message printed



---

Applications

Jewelry Shop Security

Museum Object Protection

Smart Home Security

Office Equipment Monitoring

ATM Monitoring Systems

Industrial Safety Systems



---

Advantages

Low-cost security system

Real-time detection

Smart object monitoring

Easy hardware integration

Expandable to IoT systems

Beginner-friendly implementation



---

Future Enhancements

ESP32-CAM standalone version

Telegram mobile alerts

Face recognition

Human detection using YOLO

Cloud monitoring dashboard

Intruder image capture

Battery-powered operation



---

Learning Outcomes

This project helped in understanding:

Computer Vision

Image Processing

OpenCV

Embedded Systems

Serial Communication

Python-Arduino Integration

Real-Time Monitoring Systems

AI + IoT Integration



---

Repository Structure

AI-Object-Tampering-Detection-System
│
├── python-code
│   └── object_tamper_detection.py
│
├── arduino-code
│   └── object_alarm_system.ino
│
├── project-images
│   └── project_setup.jpg
│
├── report
│   └── project_report.pdf
│
└── README.md


---

Author

Mani
EEE Student | AI + Embedded Systems Enthusiast
