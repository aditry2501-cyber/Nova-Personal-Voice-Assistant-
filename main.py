import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import musiclibrary


# Initialize recognizer (no need for global engine since speak() creates its own)
recognizer = sr.Recognizer()

# Give you more time between phrases
recognizer.pause_threshold = 1.0


def speak(text):
    """Speak the given text aloud."""
    print(f"Speaking: {text}")
    # Re-initialize pyttsx3 each time to avoid audio device lock issues
    local_engine = pyttsx3.init('sapi5')
    voices = local_engine.getProperty('voices')
    local_engine.setProperty('voice', voices[0].id)  # or [1] for female
    local_engine.setProperty('rate', 170)
    local_engine.say(text)
    local_engine.runAndWait()
    local_engine.stop()


def processCommand(command):
    """Process the recognized voice command."""
    print(f"Command received: {command.lower()}")

    # Use if/elif/else so it doesn't always fall to the last 'else'
    if "open google" in command.lower():
        speak("Opening Google for you.")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command.lower():
        speak("Opening Facebook for you.")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command.lower():
        speak("Opening LinkedIn for you.")
        webbrowser.open("https://in.linkedin.com")

    elif "open youtube" in command.lower():
        speak("Opening YouTube for you.")
        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in command.lower():
        speak("Opening Instagram for you.")
        webbrowser.open("https://www.instagram.com")

    elif "open gmail" in command.lower():
        speak("Opening Gmail for you.")
        webbrowser.open("https://www.gmail.com")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    else:
        speak("Sorry, I don't know how to do that yet.")


if __name__ == "__main__":
    speak("Initializing Nova")

    while True:
        with sr.Microphone() as source:
            print("Calibrating for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Say 'Nova' to activate.")

            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print(f"Heard: '{word}'")

                if "nova" in word.lower():
                    # Wake response
                    speak("Yes, How can i Help you?")
                    print("Listening for a command...")

                    # Give a longer pause so the TTS fully finishes before mic reopens
                    time.sleep(0.5)  # Removed engine.stop() - it was causing the issue

                    with sr.Microphone() as command_source:
                        recognizer.adjust_for_ambient_noise(command_source, duration=0.5)
                        print("Listening for your command...")
                        audio_command = recognizer.listen(command_source, timeout=5)
                        command = recognizer.recognize_google(audio_command)
                        processCommand(command)

            except sr.UnknownValueError:
                pass  # simply ignore background noise
            except sr.WaitTimeoutError:
                print("Listening timed out, waiting again...")
            except Exception as e:
                print(f"An error occurred: {e}")



