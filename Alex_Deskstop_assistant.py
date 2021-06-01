import pyttsx3
import speech_recognition
import wikipedia
import webbrowser
import random
import os
import datetime
speaker = pyttsx3.init("sapi5")
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

email_dict = {"friend1": "friend171@gmail.com", "friend2": "Friend211@gmail.com"}

def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()


def wish_me():
    hr = datetime.datetime.now().hour
    """This function wishes the user when he uses the AI assistant!!"""
    hour = int(datetime.datetime.now().hour)
    if hr >= 0 and hr <= 12:
        speak("Good morning Sir!!")

    elif hr > 12 and hr < 17:
        speak("Good afternoon sir!!")
    else:
        speak("Good evening sir!!")
    speak("My name is Alex!! How may I help you??")


def take_command():
    p = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        """Records the voice via microphone"""
        print("Listening...")
        p.pause_threshold = 1
        audio = p.listen(source)
    try:
        print("Recognizing...")
        command = p.recognize_google(audio,language="en-in")
        print(f"User asked for:{command}")
    except Exception as e:
        print("Not recognized... say it again please...")
        return "none"
    return command


if __name__ == '__main__':
    wish_me()

    query = take_command().lower()

    if "wikipedia" in query:
        query = query.replace("wikipedia", " ")
        result = wikipedia.summary(query, sentences=4)
        speak("According to wikipedia..")
        speak(result)

    elif "google" in query:
        speak("Give me a second please")
        webbrowser.open("google.com")

    elif "youtube" in query:
        speak("Give me a second please")
        webbrowser.open("youtube.com")

    elif "play music" in query:
        music_folder = "D://Music"
        available_songs = os.listdir(music_folder)
        length = len(available_songs)
        song_position = random.randint(0, length-1)
        os.startfile(os.path.join(music_folder, available_songs[song_position]))

    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Currently the time is:{time}")

    elif "open pycharm" in query:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
        os.startfile(path)












