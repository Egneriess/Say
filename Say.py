import pyttsx3
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say(sys.argv[1:])
engine.runAndWait()
