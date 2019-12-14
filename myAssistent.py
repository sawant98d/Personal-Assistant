
import pyttsx3
import datetime
import speech_recognition as sr  
import setuptools
import wikipedia   # for finding info on wikipedia
import webbrowser  # searching sites on browser
import os          # used to open the os application
import smtplib     # for email sending

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=16 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak('My Name is Krrish. I am assistent of sawant. How may I help you?')

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print('Recognizing. . . ')
        query = r.recognize_google(audio, language='en-In')    
        print(f"User said: {query}\n")        
    except:
        #print(e)
        print('Say that again please....')
        return 'None'
    return query

# this fun actually send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sawant97d@gmail.com','i3codding')
    server.sendmail('sawant97d@gmail.com',to, content)
    server.close()
    



if __name__ == "__main__":
    # wish at once when starts application
    wishMe()
    while True :
    #if True:

        # logic fro executing taks based on query
        query = takeCommand().lower()
        print(query)
        # finding wikipedia
        if query == None:
            speak('Sir, please speak something. I am listening')
        elif 'wikipedia' in query:
            speak('Searching')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)            

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query :
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = "H:\\Video"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  # starts first song file

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        print(query,query,query,query)   


        if 'netbeans' in query:
            os.startfile("C:\\Program Files (x86)\\NetBeans 8.2\\bin\\netbeans.exe")

        if 'email' or 'email to sawant' in query:
        
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "sawant65d@gmail.com"
                sendEmail(to,content)
                speak('Email has send, sir')
            except Exception as ex:
                print(ex)
                speak('Sorry, sir I am not able to send the mail')
                speak('Try again')
    
        elif 'name' or 'who you are' in query:
            
            pass
        
        elif 'thank you' in query :
            speak("It's my pleasure, Sir")                            



        
# pip install pyttsx3
# pip install  speechRecognition
# pip install wikipedia
