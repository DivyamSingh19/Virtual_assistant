import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer() #recognise your voice

voice = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)   #this is used to change the voicde of assistant

def take_command():
 try:
     with sr.Microphone() as sourse:
          print("listening")
          voice = listener.listen(source)
          #voice to text
          command = listener.recognize_google(voice)
          if 'alexa' in command:
              command = command.replace('alexa', '') #removes alexa from command
              print(command)
 except:
     pass

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
       song=command.replace('play','')
       talk('playing' +song)
       pywhatkit.playonyt(song)

run_alexa()