import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)
def speak(audio): 
   engine.say(audio)
   engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")  
    else:
        speak("good evening")
    speak("I am Jarvis Sir. Please tell me how may I help you")          

def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as Source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(Source)   
     try:
         print("Recognizing...")
         query=r.recognize_google(audio, language='en-in')
         print(f"User Said: {query}\n") 
     except Exception as e:    
        print("say that again please...")
        return "None"
     return query 

if __name__=="__main__":
    wishme()
    while True:
    # if 1:  
     query=takecommand().lower()
     if 'wikipedia' in query:
      speak('Searching wikipedia..')
      results=wikipedia.summary(query,sentences=2)
      speak("According to wikipedia")
      print(results)
      speak(results)
      
     elif 'google' in query:
      webbrowser.open("google.com")  

     elif 'youtube' in query:
      webbrowser.open("youtube.com")   

     elif 'facebook' in query:
      webbrowser.open("facebook.com")  

     elif 'my college website' in query:
      webbrowser.open("https://www.srmist.edu.in/") 

     elif 'play music' in query:     
       music="D:\\songs\\2k18 Rg"
       songs=os.listdir(music)
       print(songs)
       os.startfile(os.path.join(music,songs[24]))
     elif 'time' in query:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {time}" )
     elif 'open code' in query:
        codepath="C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(codepath)      
     elif  'my'  in query:
      picpath="D:\\new delhi"
      listpicpath=os.listdir(picpath)
      os.startfile(os.path.join(picpath,listpicpath[23]))
     elif  'family'  in query:
      picpath="D:\\sdcard september\\DCIM\\Camera"
      listpicpath=os.listdir(picpath)
      #  os.startfile(os.path.join(picpath,listpicpath[23])) 
      os.startfile(picpath)

     
