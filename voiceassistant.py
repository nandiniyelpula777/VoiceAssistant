import speech_recognition as sprc
import wikipedia
import pyttsx3
import datetime

# ✅ Define speak function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# The voice assistant name is Babji
babji = pyttsx3.init()
speechrecognizer = sprc.Recognizer()

with sprc.Microphone() as source:
    speak('Hello, I am Babji. How can I help you?')
    speechrecognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your command...')
    recordedaudio = speechrecognizer.listen(source)
    print('Command received')

try:
    print('Working on your command...')
    text = speechrecognizer.recognize_google(recordedaudio, language='en-US')
    print(f'Your Command: {text}')

    if "hello" in text.lower():
        speak('Hello! How can I assist you today?')
    elif "current date" in text.lower():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f'Today\'s date is {current_date}')
    elif "current time" in text.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'The current time is {current_time}')
    else:
        try:
            wikisearch = wikipedia.summary(text, sentences=2)
            print('Wikipedia Summary:', wikisearch)
            speak(wikisearch)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("I couldn't find any information on that.")

except Exception as ex:
    print("Error:", ex)
    speak('I encountered an error. Please try again.')
