  
import wolframalpha
import wikipedia
import pyttsx3
import pyjokes
import pywhatkit
import time
import speech_recognition as sr

engine = pyttsx3.init()
listener = sr.Recognizer()

with sr.Microphone() as source:
    listener.adjust_for_ambient_noise(source, duration=0.2)
    sound = listener.listen(source)
    text = listener.recognize_google(sound)
    text = text.lower()
    print(text)


def func():
    try:
        if "what" in text:
            text.replace("what is","")
            app_id = ("YOUR API KEY")
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            engine.say(answer)
            engine.runAndWait()

        elif "who" in text:
            e = wikipedia.summary(text)
            engine.say(e)
            engine.runAndWait()

        elif "why" in text:
            app_id = ("YOUR API KEY")
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            engine.say(answer)
            engine.runAndWait()

        elif "where" in text:
            app_id = ("YOUR API KEY")
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            engine.say(answer)
            engine.runAndWait()

        elif "when" in text:
            app_id = ("YOUR API KEY")
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            engine.say(answer)
            engine.runAndWait()

        elif "how" in text:
            text.replace("what is","")
            app_id = ("YOUR API KEY")
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            engine.say(answer)
            engine.runAndWait()
        elif "joke" in text:
            j = pyjokes.get_joke()
            engine.say(j)
            engine.runAndWait()

        elif "play" in text:
            pywhatkit.playonyt(text)

        elif "hello" in text:
            engine.say("Hello! How are you!")
            engine.runAndWait()

        elif "what" and "time" in text:
            t = time.localtime()
            ct = t.strftime("%H,%M,%S")
            engine.say(ct)
            engine.runAndWait()
        elif "how are you" in text:
            engine.say("I am doing well")
            engine.runAndWait()
        elif "who are you" in text:
            engine.say("I am your virtual assistant.")
            engine.runAndWait()
    except:
        engine.say("Could you say that again?")
        engine.runAndWait()


func()