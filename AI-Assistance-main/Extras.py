import pyautogui
import pyautogui
import psutil
import pyttsx3
import webbrowser
import pyjokes
import speech_recognition as sr

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


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\vishal sharma\\Desktop\\code\\DA Project\\DataBase\\Screenshots") # isme error h

# cpu usage and battery update function
def cpu_usage():
    usage = str(psutil.cpu_percent())
    print("Cpu utilization is "+usage+"%")
    Speak("Cpu utilization is"+usage+"%")
    battery = psutil.sensors_battery()
    print("Battery percentaeg is:",battery.percent)
    Speak("Battery percentage is: ")
    Speak(battery.percent)


# battery percentage
def battery_per():
    battery = psutil.sensors_battery()
    print("Battery percentaeg is:",battery.percent)
    Speak("Battery percentage is: ",battery.percent)

# jokes function
def jokes():
    Speak(pyjokes.get_joke())

def open(website):
    webbrowser.open(website)