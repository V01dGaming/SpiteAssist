import speech_recognition as sr
import time as t
import webbrowser as web
import secrets as sec
import os
import sys
import winsound
import pyttsx3

## Speech
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("rate", 170)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM"
engine.setProperty("voice", voice_id)

## Just phrases
OpeningResponse = ["How's it going?", "How are things?", "What's up?", "How's life treating you?", "How's your day?", "What's new?", "How's everything?", "How are you feeling?", "How goes it?", "How's your day been?", "What's happening?", "How's your world?", "How's your day going so far?", "How are you today?", "How's your week been?", "How's your weekend going?", "How's your morning?", "How's your afternoon?", "How's your evening?", "How are you holding up?"]
Steamoptions = ["open steam", "start steam", "run steam", "please open steam", "please start steam", "please run steam", "open steam please", "start steam please", "run steam please"]
Discordoptions = ["open discord", "start discord", "run discord", "please open discord", "please start discord", "please run discord", "open discord please", "start discord please", "run discord please"]
Restartoptions = ["restart", "please restart", "restart please"]
Crunchyrolloptions = ["open crunchyroll", "open my anime", "open anime", "please open crunchyroll", "please open my anime", "please open anime", "open crunchyroll please", "open my anime please", "open anime please"]
Internetoptions = ["open internet", "open the internet", "open chrome", "open the browser", "open the web", "open browser", "open web", "please open internet", "please open the internet", "please open chrome", "please open the browser", "please open the web", "please open browser", "please open web", "open internet please", "open the internet please", "open chrome please", "open the browser please", "open the web please", "open browser please", "open web please"]
Shutdownoptions = ["shut down", "shutdown", "power off", "turn off", "power down", "terminate", "shut down please", "shutdown please", "power off please", "turn off please", "power down please", "terminate please", "please shut down", "please shutdown", "please power off", "please turn off", "please power down", "please terminate"]
Nevermind = ["nevermind", "never mind"]
Wakeword = ["zero", "hey zero"]

#Phrases - 1 phrase provided by human, the rest provided by ChatGPT
openanime = ["I trust you're having a delightful time indulging in the world of anime.", "I hope your anime journey is filled with joy and wonder.", "Do you have any tech questions on your mind today?"]
howmayihelp = ["How can I be of service to you today?", "How may I assist you with your queries today?", "Feel free to ask anything; I'm here to help."]
opengoogle = ["May you discover what you seek on the vast expanse of the internet!",]
shutdownpls = ["Farewell for now! I look forward to our future interactions.",]
discordpls = ["Getting ready to dive into the world of Discord, I see!"]
steampls = ["Launching Steam and ready for some gaming fun, are we?"]
restartpls = ["Certainly, Zero is initiating a self-reboot. If you have any questions or need assistance once Zero is back online, please don't hesitate to ask.",]

web.register("chrome", None, web.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

def speak(txt):
    pyttsx3.speak(txt)

def clr1():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def clr():
    os.execv(sys.executable, ["python"] + sys.argv)
    exit()

def speech_recognition1():
    clr1()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for Wake Word...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            txt1 = (r.recognize_google(audio)).lower()
            if txt1 in Wakeword:
                speak("Wake word detected")
                t.sleep(1)
                speech_recognition2()
        except sr.UnknownValueError:
        #    speak("Unable to understand speech")
        #    t.sleep(2)
            clr()
        except sr.RequestError as e:
            print("Error:", e)
        speech_recognition1()

def speech_recognition2():
    clr1()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        P=(sec.choice(howmayihelp))
        print("Listening...")
        speak(P)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            txt = (r.recognize_google(audio)).lower()
            if txt in Internetoptions:
                P=(sec.choice(opengoogle))
                speak("Opening Chrome... ")
                t.sleep(1)
                speak(P)
                web.get("chrome").open("https://www.google.com/")
                t.sleep(2)
                clr()
            elif txt in Steamoptions:
                speak("Opening Steam...")
                os.system("start Steam")
                t.sleep(2)
                clr()
            elif txt in Crunchyrolloptions:
                P=(sec.choice(openanime))
                speak("Opening Crunchy roll...")
                t.sleep(1)
                speak(P)
                web.get("chrome").open("https://www.crunchyroll.com/")
                t.sleep(2)
                clr()
            elif txt in Discordoptions:
                speak("Opening Discord...")
                os.system("start Discord")
                t.sleep(2)
                clr()
            elif txt in Restartoptions:
                speak("restarting...")
                clr()
            elif txt in Shutdownoptions:
                P=(sec.choice(shutdownpls))
                speak("Shutting down...")
                t.sleep(1)
                speak(P)
                t.sleep(2)
                quit()
            elif txt in Nevermind:
                t.sleep(2)
                clr()
        except sr.UnknownValueError:
        #    speak("Unable to understand speech")
        #    t.sleep(1)
            clr()
        except sr.RequestError as e:
            print("Error:", e)
        clr()
        speech_recognition1()

os.system("title Zer0")
#P=(sec.choice(OpeningResponse))
#print(P)
#speak(P)
speech_recognition1()
