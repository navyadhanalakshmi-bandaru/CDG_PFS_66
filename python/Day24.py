# ============================================================
# Day 24: Virtual Assistant Project
# ============================================================
# SubTopics:
# 1. Voice Commands
# 2. Speech Recognition Basics
# 3. Python Assistant Mini Project
#
# Required libraries:
# pip install SpeechRecognition pyttsx3 PyAudio
# ============================================================


# ============================================================
# 1. IMPORT MODULES
# ============================================================

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# ============================================================
# 2. TEXT TO SPEECH
# ============================================================

# Initialize text-to-speech engine

engine = pyttsx3.init()


def speak(text):

    print("Assistant:", text)

    engine.say(text)

    engine.runAndWait()


# Test voice

speak("Hello! I am your Python assistant.")


# ============================================================
# 3. SPEECH RECOGNITION BASICS
# ============================================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:

        print("Sorry, I could not understand.")

        return ""

    except sr.RequestError:

        print("Speech recognition service is unavailable.")

        return ""


# ============================================================
# 4. VOICE COMMANDS
# ============================================================

def get_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak("The current time is " + current_time)


def get_date():

    current_date = datetime.datetime.now().strftime("%d %B %Y")

    speak("Today's date is " + current_date)


# ============================================================
# 5. VIRTUAL ASSISTANT
# ============================================================

def virtual_assistant():

    speak("How can I help you?")

    while True:

        command = listen()


        # ----------------------------------------------------
        # Time
        # ----------------------------------------------------

        if "time" in command:

            get_time()


        # ----------------------------------------------------
        # Date
        # ----------------------------------------------------

        elif "date" in command:

            get_date()


        # ----------------------------------------------------
        # Open Google
        # ----------------------------------------------------

        elif "open google" in command:

            speak("Opening Google.")

            webbrowser.open("https://www.google.com")


        # ----------------------------------------------------
        # Open YouTube
        # ----------------------------------------------------

        elif "open youtube" in command:

            speak("Opening YouTube.")

            webbrowser.open("https://www.youtube.com")


        # ----------------------------------------------------
        # Search Google
        # ----------------------------------------------------

        elif command.startswith("search"):

            search_text = command.replace("search", "").strip()

            if search_text:

                speak("Searching for " + search_text)

                url = (
                    "https://www.google.com/search?q="
                    + search_text.replace(" ", "+")
                )

                webbrowser.open(url)

            else:

                speak("Please tell me what you want to search.")


        # ----------------------------------------------------
        # Greeting
        # ----------------------------------------------------

        elif "hello" in command or "hi" in command:

            speak("Hello! How can I help you?")


        # ----------------------------------------------------
        # Name
        # ----------------------------------------------------

        elif "your name" in command:

            speak("I am your Python virtual assistant.")


        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif (
            "exit" in command
            or "quit" in command
            or "stop" in command
            or "goodbye" in command
        ):

            speak("Goodbye! Have a nice day.")

            break


        # ----------------------------------------------------
        # Unknown command
        # ----------------------------------------------------

        elif command:

            speak("Sorry, I don't know that command.")


# ============================================================
# 6. RUN ASSISTANT
# ============================================================

if __name__ == "__main__":

    virtual_assistant()


# ============================================================
# END OF DAY 24
# ============================================================