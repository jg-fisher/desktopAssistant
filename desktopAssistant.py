#desktop assistant

from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser

#speaks audio passed as argument
def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('audio.mp3')

#listens for commands
def myCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('I am ready for your command!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        assistant(myCommand())
        
    return command

#if statements for executing commands
def assistant(command):
    
    if 'open Reddit machine learning' in command:
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = 'https://www.reddit.com/r/machinelearning/'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chillin bro')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())



        
        
        




