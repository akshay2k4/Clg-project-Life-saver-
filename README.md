# 🎓 Life Saver Project: Door-Activated Study Mode

An automated system to enhance focus and productivity by switching your computer to **study mode** the moment someone enters your room.

---

## 🧠 Overview

This project automatically redirects your computer from distracting content (like games or social media) to a **designated study resource** (website, document, or app) whenever the door is opened.

Using an **IR sensor**, **Arduino Uno**, and a **Python script**, this hands-free setup minimizes distractions and encourages focus.

---

## 🔑 Key Features

- 🚪 **Automatic Study Trigger**: Detects when the door opens and instantly opens a study resource.
- 🔄 **Hardware-Software Integration**: Combines Arduino (hardware) and Python (software).
- ⚙️ **Customizable Setup**: Easily modify the Python script to open any site or file you want.

---

## 🔧 Hardware Components

| Component             | Description                                |
|----------------------|--------------------------------------------|
| Arduino Uno           | Microcontroller to read the IR sensor      |
| IR Presence Sensor    | Detects door opening based on IR reflection |
| Jumper Wires + USB    | For circuit connections and serial comm     |

---

## 💻 Software Components

| Software     | Use Case                                              |
|--------------|--------------------------------------------------------|
| Arduino IDE  | Upload code to Arduino                                |
| Python 3.x   | Run automation script on computer                     |
| PySerial     | Serial communication between Arduino and Python       |

Install PySerial:
```bash
pip install pyserial




🔌 Setup Instructions
Arduino Setup
Wire the IR sensor to Arduino Uno:

VCC → 5V

GND → GND

OUT → Digital Pin 7 (or as per your code)

Upload Arduino Code:

Open arduino_code.ino in Arduino IDE

Select correct board and COM port

Upload the sketch

Python Setup
Install Python and PySerial:

Download Python 3.x from python.org

Install PySerial using pip install pyserial

Configure Python Script:

Update the COM port in life_saver.py

Replace the default URL with your desired study resource (Google Classroom, Notion, PDF, etc.)

