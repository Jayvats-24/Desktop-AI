from types import coroutine
import pyttsx3
import os
import speech_recognition as sr
from Features import GoogleSearch
from win10toast import ToastNotifier
import Extras
import tkinter as tk
from tkinter import *
from tkinter.ttk import Label
from threading import Thread


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()


def TaskExe():
    while True:
        
        query = TakeCommand()
                

        if 'on google' in query:
            GoogleSearch(query)
        
        elif 'who' in query:
            GoogleSearch(query)

        elif 'what' in query:
            GoogleSearch(query)

        elif 'play' in query:
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'on youtube' in query:
            Query = query.replace("Memo","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'message' in query:
            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("Memo ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif 'shutdown' in query:
            Speak("Shutting down your Computer")
            os.system("shutdown /s /t 1")

        elif 'restart my pc' in query:
            Speak("Restarting your pc")
            os.system("shutdown /r /t 1")

        elif 'screenshot' in query:
            from Extras import screenshot
            Speak("Capturing")
            screenshot()

        elif 'cpu usage' in query:
            from Extras import cpu_usage
            Speak("Checking your system usage")
            cpu_usage()
        
        elif 'battey percentage' in query:
            from Extras import battery_per
            Speak("Analyzing Your system battery Percentage")
            battery_per()

        elif 'joke' in query:
            Speak("Searching for a joke")
            from Extras import jokes
            jokes()
        
        elif 'open' and '.com' in query:
            query=query.replace("oepn", "")
            from Extras import open
            open(query)

        elif 'space news' in query:
            Speak("Tell Me The Date For News Extracting Process .")
            Date = TakeCommand()
            from Features import DateConverter
            Value = DateConverter(Date)
            from Nasa import NasaNews
            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("memo ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:
            from Nasa import MarsImage
            MarsImage()

        elif 'track iss' in query:
            from Nasa import IssTracker
            IssTracker()

        elif 'near earth' in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:
            from Features import My_Location
            My_Location()

        elif 'where is' in query:
            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("Memo" , "")
            GoogleMaps(Place)

        elif 'class' in query:
            from Automations import OnlinClass
            Speak("Tell Me The Name Of The Class .")
            Class = TakeCommand()
            OnlinClass(Class)

        elif 'write a note' in query:
            from Automations import Notepad
            Notepad()

        elif 'dismiss' in query:
            from Automations import CloseNotepad
            CloseNotepad()

        elif 'time table' in query:
            from Automations import TimeTable
            TimeTable()

        elif 'activate the bulb' in query:
            from DataBase.HomeAuto.SmartBulb import Activate
            Activate()
            Speak("Should I Start Or Close The Bulb ?")
            step = TakeCommand()

            if 'close' in step:
                from DataBase.HomeAuto.SmartBulb import CloseLight
                CloseLight()

            elif 'start' in step:
                from DataBase.HomeAuto.SmartBulb import StartLight
                StartLight()

        elif 'corona cases' in query:
            from Features import CoronaVirus
            Speak("Which Country's Information ?")
            cccc = TakeCommand()
            CoronaVirus(cccc)

        else:
            from DataBase.ChatBot.ChatBot import ChatterBot
            reply = ChatterBot(query)
            Speak(reply)

            if 'bye' in query:
                break

            elif 'exit' in query:
                break

            elif 'go' in query:
                break

            elif 'close' in query:
                break

def create_rectangle_outline(parent, width, height, border_color="white", border_width=2):
    frame = tk.Frame(parent, width=width, height=height, borderwidth=border_width, relief="solid", background="#2C2C2C")
    return frame

def UIfunc():

    root=tk.Tk()
    root['background']='#2C2C2C'
    root.geometry('1000x1000')
    root.title("Memo AI")

    # complete the GUI part of the MEMO Assisance 
    # creating a rectangle box that will put the suggestion content
    rectangle_frame = create_rectangle_outline(root, width=900, height=300)

    lable1=Label(root,text="Welcome User, I am Memo",font=("Arial",25),foreground='white',background="#2C2C2C")
    lable1.pack(padx=20,pady=90)

    head=Label(rectangle_frame,text=" Suggestions ",foreground='white',font=("Arial",20),background='#2C2C2C')
    head.pack(padx=8,pady=8)


    eg1=Label(rectangle_frame,text=" '' 1. Google Search '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
    eg1.pack(padx=8,pady=8)


    eg2=Label(rectangle_frame,text=" '' 2. Youtube Search '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
    eg2.pack(padx=8,pady=8)

    eg3=Label(rectangle_frame,text=" '' 3. System Information '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
    eg3.pack(padx=8,pady=8)

    eg4=Label(rectangle_frame,text=" '' 4. Location Fetch '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
    eg4.pack(padx=8,pady=8)

    eg5=Label(rectangle_frame,text=" '' 5. Calling and message Capability '' ",font=("Arial",10),foreground='white',background='#2C2C2C')
    eg5.pack(padx=8,pady=8)

    rectangle_frame.pack(padx=10,pady=10)

    label=Label(root,text=" I am Listening Whatever You Say.....",font=("Arial",20),foreground='white',background='#2C2C2C')
    label.pack(padx=0,pady=90)

    label=Label(root,text="For better Experience Keep in touch with Terminal window",font=("Arial",15),foreground='white',background='#2C2C2C')
    label.pack(padx=0,pady=0)
    
    # 1. Create a suggestion box and place some examples 
    # 2.place a gif of mic at the below of the suggession box and place it in center 
    
    root.mainloop()


    


if __name__ == "__main__":    
    # runnning the UI part in a thread
    uithread=Thread(target=UIfunc) 
    uithread.start()
    
    # running the ai in main thread
    TaskExe()
    