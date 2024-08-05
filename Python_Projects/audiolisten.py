import speech_recognition as sr
import os

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while True:
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                print("Adjusting for ambient noise...")
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listen for the user's input
                print("Listening...")
                audio2 = r.listen(source2)

                # Using Google to recognize audio
                print("Recognizing...")
                MyText = r.recognize_google(audio2)
                print("You said:", MyText)

                if MyText.lower() == "stop":
                    print("Stop command received. Exiting...")
                    return "stop"
                return MyText 
        except sr.UnknownValueError:
            print("Unknown error occurred. Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return None

def output_text(text):
    try:
        print("Saving to file:", text)
        # Save the data in a text file
        with open(os.path.join("D:/","output.txt"), "a") as f:
            f.write(text)
            # Add a line if we say multiple lines
            f.write("\n")
        print("Text saved to file.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    return

while True:
    text = record_text()
    if text:
        if text.lower() == "stop":
            break
        output_text(text)
        print("Wrote text")
        
        
 print("Hello world")
