import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your virtual assistant. Laura')
engine.say('Let me give a hand, MASTERR')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'system' in command:
                command = command.replace('system', '')
                print(command)

    except:
        pass
    return command


def run_system():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('It is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        pywhatkit.search(info)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    # daily conversation
    elif 'good morning' in command:
        talk('Good Morning, Master!')
    elif 'how are you' in command:
        talk('I am in my best condition, Master')
    elif 'introduce' in command:
        talk('Let me introduce myself. My name is Veldana. I am virtual assistant!. '
             'I am created on Saturday, September 4th 2021. My master is Fadli ')
    elif 'call my name' in command:
        talk('Hello Fadli !.')
    elif 'hmm' in command:
        talk('Are you okay, Master!')
    elif 'fine' in command:
        talk('May God Bless you, Master')
    elif 'thank you' in command:
        talk('Your welcome, Master.')

    # command power
    elif 'fire the flames' in command:
        talk('Okay. Enhance Armament. Generate fire flames. Discharge!!!')
    elif 'attack the enemy' in command:
        talk('Yes sir. Prepare weapons, target enemies. Enemy Locked. Fire!!!.')
    elif 'enemy' in command:
        talk('Okay. Identification Local Area. ENEMY SPOTTED!!!')
    elif 'mistake' in command:
        talk('Yes Sir!. Please Forgive me. Master!')
    elif 'enhance armament' in command:
        talk('yes sir, system call. Enhance Armament!')
    else:
        talk('Please say the command again Master.')

while True:
    run_system()