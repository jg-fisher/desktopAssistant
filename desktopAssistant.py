    #desktop assistant

from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

#speaks audio passed as argument
def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#ffplay

#listens for commands
def myCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('I am ready for your next command!')
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
    
    if 'open Reddit python' in command:
        chrome_path = "/usr/bin/google-chrome"
        url = 'https://www.reddit.com/r/python/'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Just doing my thing')

    if 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('jfishersolutions', 'dallas40')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

            
talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())



        
        
        




