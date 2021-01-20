import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

#Change from default voice to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as sourse:
            print('Listening...')
            voice = listener.listen(sourse)
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

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'give me info about' in command:
        question = command.replace('give me info about', '')
        #Darla will print the first line of info from Wikipedia
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    #If Darla doesn't understand the command or if you ask her something that she doesn't know
    else:
        talk('Please say that command again Ana.')

while True:
    run_darla()
