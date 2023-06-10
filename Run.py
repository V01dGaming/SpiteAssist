import speech_recognition as sr
import time as t
import webbrowser as web
import secrets as sec
import os
import sys

Steamoptions = ["open steam", "start steam", "run steam", "please open steam", "please start steam", "please run steam", "open steam please", "start steam please", "run steam please"]
Discordoptions = ["open discord", "start discord", "run discord", "please open discord", "please start discord", "please run discord", "open discord please", "start discord please", "run discord please"]
Restartoptions = ["restart", "please restart", "restart please"]
Crunchyrolloptions = ["open crunchyroll", "open my anime", "open anime", "please open crunchyroll", "please open my anime", "please open anime", "open crunchyroll please", "open my anime please", "open anime please"]
Internetoptions = ["open internet", "open the internet", "open chrome", "open the browser", "open the web", "open browser", "open web", "please open internet", "please open the internet", "please open chrome", "please open the browser", "please open the web", "please open browser", "please open web", "open internet please", "open the internet please", "open chrome please", "open the browser please", "open the web please", "open browser please", "open web please"]
Shutdownoptions = ["shut down", "shutdown", "power off", "turn off", "power down", "terminate", "shut down please", "shutdown please", "power off please", "turn off please", "power down please", "terminate please", "please shut down", "please shutdown", "please power off", "please turn off", "please power down", "please terminate"]
Wakeword = ["spite", "hey spite"]

#Phrases - 1 phrase provided by human, the rest provided by ChatGPT
openanime = ["I hope you enjoy your anime!", "May you have a delightful time watching your anime!", "Wishing you a wonderful experience with your anime!", "I hope your anime brings you immense enjoyment!", "May your anime viewing be filled with joy and satisfaction!"]
howmayihelp = ["What can I do for you?", "How may I assist you?", "How can I be of service?", "In what way can I help you?", "What do you need me to do?", "How may I be of assistance to you?", "Is there anything specific I can help you with?", "What is it that you require from me?", "How can I support you in your endeavors?", "Do you have any particular needs or requests that I can address?"]
opengoogle = ["I hope you find what you are looking for!", "May your search yield the results you desire!", "Wishing you success in finding what you seek!", "Here's to discovering exactly what you're after!", "Sending positive vibes your way as you embark on your quest for what you need!"]
shutdownpls = ["Goodbye, I hope to see you soon!", "Farewell, looking forward to our next encounter!", "Take care, I eagerly await our next meeting!", "Goodbye, hoping for a swift reunion!", "Until we meet again, I'll be anticipating our next rendezvous!"]

web.register("chrome", None, web.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))


def clr1():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def clr():
    os.execl(sys.executable, sys.executable, *sys.argv)
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
                print("Wake word detected: ", txt1)
                t.sleep(1)
                speech_recognition2()
        except sr.UnknownValueError:
            print("Unable to understand speech")
            t.sleep(2)
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
        print(P)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            txt = (r.recognize_google(audio)).lower()
            print("You said: ", txt)
            if txt in Internetoptions:
                P=(sec.choice(opengoogle))
                print("Opening Chrome... ")
                print(P)
                web.get("chrome").open("https://www.google.com/")
                t.sleep(2)
                clr()
            elif txt in Steamoptions:
                print("Opening Steam...")
                os.system("start Steam")
                t.sleep(2)
                clr()
            elif txt in Crunchyrolloptions:
                P=(sec.choice(openanime))
                print("Opening Crunchyroll...")
                print(P)
                web.get("chrome").open("https://www.crunchyroll.com/")
                t.sleep(2)
                clr()
            elif txt in Discordoptions:
                print("Opening Discord...")
                os.system("start Discord")
                t.sleep(2)
                clr()
            elif txt in Restartoptions:
                print("restarting...")
                clr()
            elif txt in Shutdownoptions:
                P=(sec.choice(shutdownpls))
                print("Shuting down...")
                print(P)
                t.sleep(2)
                quit()
        except sr.UnknownValueError:
            print("Unable to understand speech")
            t.sleep(2)
            clr()
        except sr.RequestError as e:
            print("Error:", e)
        clr()
        speech_recognition1()

os.system("title SpiteAssist")
speech_recognition1()
