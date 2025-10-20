import serial.tools.list_ports
import speech_recognition as sr
import pyttsx3


ports = serial.tools.list_ports.comports()
portsList = [port.device for port in ports]
print("Available COM ports:", portsList)

com = input("Select COM Port for Arduino (e.g., COM4): ")


try:
    ser = serial.Serial(port=com, baudrate=9600, timeout=1)
    print(f"Connected to {com}")
except serial.SerialException as e:
    print(f"Error: Could not open port {com}. {e}")
    exit()


recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            try:
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized: {text}")

                ser.write(text.encode('utf-8'))

                if text == 'exit' or text == "exits":
                    print("Exiting...")
                    ser.close()
                    exit()

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
    except KeyboardInterrupt:
        print("Interrupted by user")
        ser.close()
        break
