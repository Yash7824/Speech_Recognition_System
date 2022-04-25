import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import pyjokes
import smtplib
# import asyncio
# from winrt.windows.devices import radios

engine = pyttsx3.init('sapi5')
#getting details of current voice
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    #Without this command, speech will not be audible to us.
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour >=0 and hour < 12:
        speak("Good Morning!")
    
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")
    
    speak("I am Alexa, how may I help you sir?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio) #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fakeemail7824@gmail.com', 'your-password')
    server.sendmail('fakeemail7824@gmail.com', to, content)
    server.close()

# async def bluetooth_power(turn_on):
#     all_radios = await radios.Radio.get_radios_async()
#     for this_radio in all_radios:
#         if this_radio.kind == radios.RadioKind.BLUETOOTH:
#             if turn_on:
#                 result = await this_radio.set_state_async(radios.RadioState.ON)
#             else:
#                 result = await this_radio.set_state_async(radios.RadioState.OFF)

if __name__=="__main__" :
    speak("Hello")
    wishme()
    
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open Vellore' in query:
            webbrowser.open("https://vit.ac.in")

        elif 'open V top' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")
        
        elif 'open Vtop' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")

        elif 'open bi top' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")

        elif 'open beta' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")

        elif 'open the door' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")
            
        elif 'open we talk' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/home?lang=en")

        elif 'open w3 schools' in query:
            webbrowser.open("https://www.w3schools.com/default.asp")
        
        elif 'human computer interaction folder' in query:
            hci_dir = 'D:\\YASH\\5th Sem\\Human-Computer-Interaction\\Theory'
            os.startfile(hci_dir)

        elif 'open vs code' in query:
            vs_code = 'C:\\Users\\yashr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(vs_code)

        elif 'open spotify' in query:
            spotify = 'C:\\Users\\yashr\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(spotify)

        elif 'open calculator' in query:
            calculator = 'C:\\Windows\\System32\\calc.exe'
            os.startfile(calculator)
        
        elif 'open notepad' in query:
            notepad = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(notepad)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'jokes' in query:
            print(pyjokes.get_joke())
        
        elif 'email to Yash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashr@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Yash, I am not able to send this email") 

        elif 'open star uml' in query:
            uml = 'C:\\Program Files\\StarUML\\StarUML.exe'
            os.startfile(uml)

        elif 'open word' in query:
            word = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word)

        elif 'open excel' in query:
            excel = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"'
            os.startfile(excel)

        elif 'open powerpoint' in query:
            powerpoint = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"'
            os.startfile(powerpoint)
          
        

        
        
        


        

 