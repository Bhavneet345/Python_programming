def speak(str):

    from win32com.client import Dispatch
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(str)


if __name__ == '__main__':
    speak("Hello!!Today's news headlines are")
    import json
    import requests
    res = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9d65b541be574e9293a1c7e3ad18a344")
    new = res.text
    news_dict = json.loads(new)
    arts = news_dict["articles"]
    for data in arts:
        speak(data["title"])


