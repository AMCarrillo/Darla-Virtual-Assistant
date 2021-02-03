import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha
import webbrowser
import sys

app_id = 'RP3TEQ-UUE5G24J9W'
client = wolframalpha.Client('RP3TEQ-UUE5G24J9W')

listener = sr.Recognizer()
engine = pyttsx3.init()

#Change from default voice to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#Voice speed
engine.setProperty("rate", 178)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def Greet_me():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        talk('Good Morning! I am Darla, your virtual assistant. How may I help you?')

    if currentH >= 12 and currentH < 18:
        talk('Good Afternoon! I am Darla, your virtual assistant. How may I help you?')

    if currentH >= 18 and currentH !=0:
        talk('Good Evening! I am Darla, your virtual assistant. How may I help you?')

Greet_me()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'darla' in command:
                command = command.replace('darla', '')
                print(command)
    except:
        pass
    return command

def run_darla():
    
        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            #Darla will search on Youtube for the song
            pywhatkit.playonyt(song)

        #Two parameters: 1. URL of the webpage. 2. How to open the page: 
        # new=1: open the webpage in a new browser window
        # new=2: open the webpage in a new tab

        elif 'open google' in command:
            talk('opening')
            webbrowser.open('http://google.com', new=2)

        elif 'open python school' in command:
            talk('opening')
            webbrowser.open('https://www.w3schools.com/python/default.asp', new=1)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'give me information about' in command:
            question = command.replace('give me information about', '')
            #Darla will say the first line of info
            try:
                info = wikipedia.summary(question, 1)
                talk('Searching on Wikipedia')
                talk(info)

            except:
                res = client.query(question)
                info = next(res.info).text
                talk('Searching on Wolframalpha')
                talk(info)


        elif 'joke' in command:
            talk(pyjokes.get_joke())
        
        elif 'nothing' in command or 'quit' in command or 'stop' in command:
            talk('okay')
            talk('Bye Ana.')
            sys.exit()

        #If Darla doesn't understand the command or if you ask her something that she doesn't know
        else:
            talk('Please say that command again Ana.')

while True:
    run_darla()
