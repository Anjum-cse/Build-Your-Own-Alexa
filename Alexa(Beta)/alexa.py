#Recquired Libararies
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

#initiate listener
#@reserved by veerIT,July-2021

listener= sr.Recognizer()
engine= pyttsx3.init()

#give it to a female voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#define speech function
def talk(text):
    engine.say(text)
    engine.runAndWait()
#listen function
def take_command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening..........')
            talk('please wait 2 second & proceed with your command!')
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command= command.lower()
            print(f"Original command: {command}")
            if 'alexa' in command:
                command=command.replace('alexa','')
            return command

    except:
        pass

def run_jara():
    command= take_command()
    print(f"Modified command: {command}")
    if command is None:
        command = "How can i help you?"

    if 'play' in command:
        song= command.replace('play','')
        print(song)
        talk('Playing it for you, honey!'+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time= datetime.datetime.now().strftime('%I-%M %p')
        talk('Currently it is' +time)

    elif "tell me about" in command:
        things= command.replace("tell me about",'')
        info= wikipedia.summary(things,1)
        print(info)
        talk('in short' +info)
    elif 'joke' in command:
        joke= pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "take care" in command:
        talk("Thank you dear, Stay safe & Blessed")

    elif "good night" in command:
        talk("good night honey, Have a sound sleep")

    elif "good morning" in command:
        talk("good morning, have a wonderful day. you need a coffee?")
    elif "exit" in command:
        sys.exit()

    else:
        talk('apologies! i didn\'t understand!')
        talk(command)
        talk("Can you please tell me again?..")
        run_jara()

while True:
    run_jara()