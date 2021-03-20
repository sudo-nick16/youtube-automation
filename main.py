import pyautogui as p
import selenium as s
import webbrowser
import pyttsx3 as ptts
import speech_recognition
import time
import io
import os
import google.cloud.speech

'''from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from IPython.display import Audio'''

speechrec = speech_recognition.Recognizer()
def stt():
    
    with speech_recognition.Microphone() as source:
        print('Listening...\n')
        audiocap = speechrec.listen(source)
        rectext = speechrec.recognize_google(audiocap)
        print(rectext)
        return rectext
def speak(text):
    engine = ptts.init()
    engine.setProperty('rate',170)
    engine.say(text)
    engine.runAndWait()

running = True

while running:
    try:
        speak("Say Something Sir")
        command = stt()
        command = command.lower()
        time.sleep(1)
        if 'open' in command and 'youtube' in command:
            print("Opening Youtube")
            speak("Opening Youtube, Sir")
            webbrowser.open("https://youtube.com/")
            ytopen = True
            search = 0
            while ytopen:
                try :
                    if search < 1:
                        speak("Say Something Sir")
                        command = stt()
                        command = command.lower()
                        search += 1
                        p.moveTo(595,163)
                        p.click()
                        print("What do you wanna look for? Sir")
                        speak("What do you wanna look for? Sir")
                        search  = stt()
                        p.write(search, interval=.20)
                        speak("Wanna look for "+ search +", Sir")
                        ans = stt()
                        ans = ans.lower()
                        if 'yes' in ans or 'yeah' in ans or 'yash' in ans or 'sure' in ans or 'h' in ans:
                            p.moveTo(1281,161)
                            p.click()
                        else:
                            speak("Please repeat, what you were looking for, Sir")
                            
                        speak("Which one of these videos do you want me to play?")
                    else:
                        speak("What do you wanna look for? Sir")
                        search  = stt()
                        p.write(search, interval=.20)
                        speak("Wanna look for "+ search +", Sir")
                        ans = stt()
                        ans = ans.lower()
                        if 'yes' in ans or 'yeah' in ans or 'yash' in ans or 'sure' in ans or 'h' in ans:
                            p.moveTo(1281,161)
                            p.click()
                        else:
                            speak("Please repeat, what you were looking for, Sir")
                            
                        speak("Which one of these videos do you want me to play?")

                except :
                    ytopen = True


           
    except:
        speak("Would you like me to go to sleep?")
        ans = stt()
        if 'yes' in ans or 'yeah' in ans or 'yash' in ans or 'sure' in ans or 'h' in ans:
            print("Exiting..")
            speak("Bye Sir")
            running = False
            exit