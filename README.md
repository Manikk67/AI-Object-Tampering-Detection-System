# AI-Object-Tampering-Detection-System

🔒 AI-Based Smart Object Tampering and Theft Detection System

📌 Overview
An AI-powered smart security system built with Python, OpenCV, and Arduino UNO for real-time object tampering and theft detection.  
Unlike traditional motion detection, this project focuses on object integrity monitoring, making it ideal for jewelry shops, museums, smart homes, and industrial safety systems.

---

✨ Features
- ✅ Real-time tampering detection  
- ✅ Computer Vision monitoring with OpenCV  
- ✅ Arduino hardware integration (LEDs + buzzer)  
- ✅ Reduced false alarms via contour filtering  
- ✅ Beginner-friendly AI + Embedded Systems project  
- ✅ Low-cost and scalable  

---

🛠️ Technologies Used

| Technology | Purpose |
|----------------|-------------|
| Python | Main programming language |
| OpenCV | Computer Vision processing |
| Arduino UNO | Hardware controller |
| PySerial | Python-Arduino communication |
| Imutils | Image resizing utility |
| Embedded Systems | Alarm integration |
| Computer Vision | Scene comparison & detection |

---

🏗️ System Architecture
`
Camera → Python OpenCV → Object Detection → Serial Communication → Arduino UNO → LED + Buzzer Alarm
`

---

🔧 Hardware Components

| Component | Quantity |
|---------------|--------------|
| Arduino UNO | 1 |
| Webcam / Laptop Camera | 1 |
| Red LED | 1 |
| Green LED | 1 |
| 220Ω Resistor | 2 |
| Active Buzzer | 1 |
| Breadboard | 1 |
| Jumper Wires | Few |
| USB Cable | 1 |

---

⚡ Circuit Connections
- Green LED → Pin 12 → Resistor → GND  
- Red LED → Pin 13 → Resistor → GND  
- Buzzer → Pin 8 → GND  

---

🔍 Working Principle
1. Webcam captures live video.  
2. First frame stored as reference frame.  
3. Each new frame → grayscale + blur.  
4. Compare with reference → detect changes.  
5. Ignore small contours to reduce false alarms.  
6. If tampering detected → Python signals Arduino.  
7. Arduino activates Red LED + Buzzer.  
8. Normal state → Green LED ON.  

---

📦 Installation
`bash
pip install opencv-python imutils pyserial
`

---

▶️ How to Run
1. Hardware Setup → Connect LEDs & buzzer.  
2. Upload Arduino Code → via Arduino IDE.  
3. Install Python Libraries → pip install.  
4. Update COM Port → in Python code.  
5. Run Python Program → monitor object.  

---

🎯 Project Output
- Normal State → Green LED ON, Buzzer OFF  
- Tampering Detected → Red LED ON, Buzzer ON, Alarm message displayed  

---

🌍 Applications
- Jewelry Security  
- Museum Object Protection  
- Smart Home Security  
- ATM Monitoring  
- Industrial Safety  

---

🚀 Advantages
- Low-cost implementation  
- Real-time detection  
- Easy hardware integration  
- Expandable to IoT systems  
- Beginner-friendly  

---

🔮 Future Enhancements
- ESP32-CAM standalone version  
- Telegram mobile alerts  
- Face recognition & YOLO human detection  
- Cloud monitoring dashboard  
- Intruder image capture  
- Battery-powered operation  

---

📚 Learning Outcomes
- Computer Vision & Image Processing  
- OpenCV basics  
- Embedded Systems integration  
- Serial Communication  
- Python-Arduino interaction  
- Real-time monitoring concepts  
- AI + IoT integration  

---

📂 Repository Structure
`
AI-Object-Tampering-Detection-System
│
├── python-code
│   └── objecttamperdetection.py
│
├── arduino-code
│   └── objectalarmsystem.ino
│
├── project-images
│   └── project_setup.jpg
│
├── report
│   └── project_report.pdf
│
└── README.md
`

---

👨‍💻 Author
Mani  
EEE Student | AI + Embedded Systems Enthusiast
