## 🤖 AI Chatbot with Arduino & Python Integration

### 📌 Overview
This project integrates an AI-powered chatbot with an **Arduino** and an **LCD display**. The chatbot listens to user input, processes the response using OpenAI's GPT model, and speaks it aloud while displaying the full response on an LCD screen.

---
## **Features**

- 🗣️ **Voice Recognition (Speech-to-Text)**
- 🔊 **Text-to-Speech (TTS) using pyttsx3**
- 📟 **LCD Display for Chatbot Responses**
- 💡 **LED Indicators for Listening & Responding**
- 🔌 **Serial Communication between Python & Arduino**
---
## 🔹 **Hardware Requirements**
- 🎥 **Arduino Uno**  
- 🎢 **16x2 I2C LCD Display** (I2C Address: 0x27 or 0x3F)  
- 🔴 **Red LED** (Indicates "Listening" Mode)  
- 🟢 **Green LED** (Indicates "Responding" Mode)  
- 🔌 **220kΩ Resistor** (Connected in series with the Red & Green LED)  
- 🛠 **Jumper Wires**  
- 🎤 **Microphone (uss Computer)**  

---

### ⚙️ Software Requirements
- **Python 3.x**
- OpenAI API Key
- Required Python Libraries:
  ```sh
  pip install openai speechrecognition pyttsx3 pyserial
  ```
- Arduino IDE (for uploading Arduino code)

### 🔌 Circuit Connections
| Component      | Arduino Pin |
|-------------- |------------|
| **LCD SDA**   | A4         |
| **LCD GNN**   | GNN        |
| **LCD VCC**   | 5v         |
| **LCD SCL**   | A5         |
| **Red LED**   | D8         |
| **Green LED** | D9         |
| **220Ω Resistor** | In Series with Green LED Red LED |

Wiring:
LED (+) (Anode) → Resistor → Arduino Pin (8 for Red, 9 for Green)
LED (-) (Cathode) → GND

---

## 🔹 **Setup Instructions**
### **1⃣ Arduino Setup**
1. Open **Arduino IDE**
2. Install required library:  
   - **LiquidCrystal_I2C** (Library Manager → Install)
3. Upload `ArduinoCode.ino` to your Arduino board.

### **2⃣ Python Setup**
1. Install **Python 3.x** & required libraries (`pip install` command above)
2. Set the correct **COM Port** in `PythonCode.py` (e.g., `COM8`)
3. Run the chatbot script:  
   ```bash
   python chatbot.py
   ```

---

## 🔹 **How It Works**
1. The system starts and displays "Chatbot Ready by Dhananjay Patil".
2. The chatbot **listens** to voice input 🎤.
3. **LEDs Indicate States:**
   - **🔴 Red LED ON:** Listening
   - **🟢 Green LED ON:** Responding
4. The **response is displayed on the LCD** 🎢 while the AI speaks 🗣️.
5. The **Green LED turns OFF** after speaking is complete.

---

## 🔹 **Example Output on LCD**
```
User: "What is AI?"
LCD:  "Artificial Intelli"
      "gence is the..."
(Speaking AI Response)
```


## Troubleshooting
- **LCD Not Displaying?** Check I2C connections and address (`0x27`).
- **No Audio Output?** Ensure speakers are connected and `pyttsx3` is installed.
- **Arduino Not Responding?** Verify the correct COM port.

## Queries & Support
For any queries, contact:
📧 Email: [patildhananajy1307@gmail.com](mailto:patildhananjay1307@gmail.com)  
🔗 LinkedIn: [Dhananjay_Patil](www.linkedin.com/in/dhananjay-patil-b25423315)


## 🔹 **Author**
**Dhananjay Patil**




