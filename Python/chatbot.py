import openai
import speech_recognition as sr
import serial
import time
import pyttsx3  # For text-to-speech
import sys

# 🔧 Replace with your OpenAI API key
API_KEY = "Your API KEY"
# 🔌 Set up Serial communication with Arduino (change COM port)
try:
    arduino = serial.Serial('COM8', 9600, timeout=1)  # Adjust COM port
    time.sleep(2)  # Wait for connection
except serial.SerialException:
    print("⚠️ Could not connect to Arduino. Check COM port!")
    sys.exit()

# 🎤 Set up Speech Recognition
recognizer = sr.Recognizer()

def chat_with_openai(prompt):
    """Sends user input to OpenAI API and returns the chatbot response."""
    try:
        openai.api_key = API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def listen_and_process():
    """Captures user voice input and converts it to text."""
    with sr.Microphone() as source:
        print("🎙️ Listening for voice input... (Say 'exit' to stop)")
        arduino.write(b"Listening\n")  # Notify Arduino (turns red LED on)
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Speech recognition service error."
        except sr.WaitTimeoutError:
            return "No speech detected."

def send_to_arduino_and_speak(response):
    """Breaks chatbot response into 32-character chunks, displays it on LCD, and speaks it."""
    chunk_size = 32  # LCD can show 32 characters at a time (16 per line)
    
    for i in range(0, len(response), chunk_size):
        chunk = response[i:i + chunk_size]  # Extract chunk of text
        
        # Send chunk to Arduino for display
        arduino.write(chunk.encode() + b"\n")
        time.sleep(1.5)  # Wait for Arduino to display it before speaking

        # 🔄 Reset and reinitialize TTS engine to prevent "run loop already started" error
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)

        # Speak only the part currently displayed on LCD
        engine.say(chunk)
        engine.runAndWait()  # Wait until speaking is done before continuing

    time.sleep(0.5)  # Small delay before listening again

def main():
    print("🤖 Chatbot is ready... (Say 'exit' to stop)")

    while True:
        user_input = listen_and_process()

        if user_input == "exit":
            print("[Chatbot] Exiting...")
            arduino.write(b"Exit\n")  # Notify Arduino to reset display
            time.sleep(2)
            arduino.close()  # Close serial connection
            print("✅ Chatbot stopped successfully.")
            sys.exit()

        # 🤖 Get AI response
        ai_response = chat_with_openai(user_input)
        print(f"[Chatbot] Response: {ai_response}")

        # 🔊 Speak response and show on LCD
        send_to_arduino_and_speak(ai_response)

if __name__ == "__main__":
    main()
