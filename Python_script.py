import serial
import webbrowser
import time

# --- Configuration ---
serial_port = 'COM10'  # Replace with your Arduino's serial port
baud_rate = 9600
study_url = "https://www.youtube.com/watch?v=jNOy11yq0gU"  # Replace with your desired study webpage
trigger_message = "DOOR_OPENED"

try:
    arduino_serial = serial.Serial(serial_port, baud_rate)
    print(f"Connected to Arduino on {serial_port}")
    time.sleep(2)  # Give time for serial connection to establish

    while True:
        if arduino_serial.in_waiting > 0:
            data = arduino_serial.readline().decode('utf-8').strip()
            print(f"Received from Arduino: '{data}'")
            if data == trigger_message:
                print(f"'{trigger_message}' received! Opening: {study_url}")
                webbrowser.open_new_tab(study_url)

except serial.SerialException as e:
    print(f"Error opening serial port '{serial_port}': {e}")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    if 'arduino_serial' in locals() and arduino_serial.is_open:
        arduino_serial.close()
        print("Serial port closed.")