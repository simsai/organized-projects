from concurrent.futures import thread
from msilib.schema import Icon
import speech_recognition as sr
import win32gui, win32con,  time , os, winapps ,winapps ,win32gui, pyautogui,win32api, win32con, pyttsx3, requests, multiprocessing, vlc
from plyer import notification
import pywhatkit as kt
from pyautogui import *
import threading 
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox 
import tkinter as tk
from distutils.command.build_scripts import first_line_re
from bs4 import BeautifulSoup
from pynput import *
import keyboard 
from vlc import *
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150) 
speech_engine = pyttsx3.init()
voices = speech_engine.getProperty('voices')


def say(phrase):
    
    

    if __name__ == '__main__':   
        p = multiprocessing.Process(target=sayFunc, args=(phrase,))

        p.start()

        
        while p.is_alive():
            time.sleep(0.5)
            if keyboard.is_pressed('q'):
                p.terminate()
            else:
                continue
        p.join()

def sayFunc(phrase):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(phrase)
    engine.runAndWait()


say("here for you")
engine.runAndWait()











notification.notify(
    title = 'simi started',
    message = 'simi started but hidden, to stop script say kill',
    app_icon = 'icon.ico',
    timeout = 20,
)



r = sr.Recognizer()
r.energy_threshold = 2000
i = 1
def stop_engine(): #ctrl+alt+h
    engine.stop()
    






def add_keyboard_evenlistener():
    def for_canonical(f):
        return lambda k: f(l.canonical(k))


    hotkey = keyboard.HotKey( keyboard.HotKey.parse('<ctrl>+<alt>+h'), stop_engine)
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
        time.sleep(5)
        l.stop()





no_of_windows = 1




class StickyNotess(Toplevel):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)
        self.xclick = 0
        self.yclick = 0

        # master (root) window
        self.overrideredirect(True)
        global no_of_windows
        self.geometry('250x250+' + str(1000+no_of_windows*(-30)) + '+' + str(100 + no_of_windows*20))
        self.config(bg = '#838383')
        self.attributes('-topmost', 'true')
        self.resizable(True,True)

        # titlebar
        self.titlebar = Frame(self, bg = '#F8F796', relief = 'flat', bd = 2)
        self.titlebar.bind('<Button-1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        self.titlebar.pack(fill = X, expand = 1, side = TOP)

        self.closebutton = Label(self.titlebar, text = 'X', bg = '#F8F7B6', relief = 'flat')
        self.closebutton.bind('<Button-1>', self.quit_window)
        self.closebutton.pack(side = RIGHT)

        self.newbutton = Label(self.titlebar, text = '+', bg = '#F8F7B6', relief = 'flat')
        self.newbutton.pack(side = LEFT)
        self.newbutton.bind('<Button-1>', self.another_window)


    
        # main text area
        self.mainarea = tkst.ScrolledText(self, bg = '#FDFDCA', font=('Comic Sans MS', 14, 'italic'), relief = 'flat', padx = 5, pady = 10,)
        self.mainarea.pack(fill = BOTH, expand = 1)
        self.mainarea.insert (tk.INSERT, res4)

        # frames to introduce shadows
        self.shadow = Frame(self).pack(side=BOTTOM)
        self.shadow = Frame(self).pack(side=RIGHT)
        
        no_of_windows += 1

    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root-self.xclick, event.y_root-self.yclick))

    def another_window(self, event):
        sticky = StickyNotess(root)

    def quit_window(self, event):
        self.closebutton.config(relief = 'flat', bd = 0)
        if(messagebox.askyesno('Delete Note?','Are you sure you want to delete this note?', parent = self)):
            global no_of_windows
            self.destroy()
            no_of_windows -= 1
            if(no_of_windows == 1):
                root.destroy()
            return
        self.closebutton.config(relief = 'flat', bd = 0, bg = '#F8F7B6')




def get_current_window():
    while 1:
        time.sleep(0.5)
        global hide
        hide = win32gui.GetForegroundWindow()

threading.Thread(target=get_current_window).start()


def simi(): 

        
            
            with sr.Microphone() as source:
                while 1:
                    try:


                        print("speak")
                        audio = r.listen(source)
                        
                        
                        
                        
                        text1 = r.recognize_google(audio, language="en-US",show_all=True )
                            

                        print("I think you said '" + r.recognize_google(audio) + "'")

                    

                        if r.recognize_google(audio) == "minimise": #minimise active app
                            win32gui.ShowWindow( hide , win32con.SW_FORCEMINIMIZE)
                            


                        elif 'close'.format(r.recognize_google(audio)) in r.recognize_google(audio): #completely kill app whose name has been said 
                            spl_word = 'close'
                            res = r.recognize_google(audio).partition(spl_word)[2]
                            closer = str(res) + str(".exe")

                            os.system('TASKKILL /F /IM ' + closer)
                            say("closed " + res)
                            engine.runAndWait()
                            
                            


                        elif 'open'.format(r.recognize_google(audio)) in r.recognize_google(audio): #open any installed application
                            spl_word2 = 'open'
                            res2 = r.recognize_google(audio).partition(spl_word2)[2]

                            for app in winapps.search_installed(res2): 
                                print(app) 
                                text = str(app)
                            


                            left = "install_location=WindowsPath('"
                            right = "'),"

                            # Output: 'string'
                            x = text[text.index(left)+len(left):text.index(right)]
                            a = str(x)
                            l = str(a) + str("/")
                            f =  str(res2.replace(" ", ""))
                            b = str(f) + str(".exe")
                            c =  str(l) + str(b)
                            print (c)

                            os.startfile(c)


                        elif 'tell me'.format(r.recognize_google(audio)) in r.recognize_google(audio): #go to any website with default browser
                            spl_word3 = 'tell me'
                            res3 = r.recognize_google(audio).partition(spl_word3)[2]
                            kt.search(res3)
                            say("looking up" + res3)
                            engine.runAndWait()



                        elif  r.recognize_google(audio) == "stop": #stop program
                            notification.notify(
                            title = 'stopped',
                            message = 'simi stopped',
                            app_icon ='icon.ico',
                            timeout = 10,
                            
                        )
                           
                            say("killing myself")
                            engine.runAndWait()
                            os.system("taskkill /im python3.10.exe /f ")

                            
                          
                            
                            
                            
                            
                            

                        elif 'note'.format(r.recognize_google(audio)) in r.recognize_google(audio): 
                            spl_word4 = 'note'
                            global res4
                            res4 = r.recognize_google(audio).partition(spl_word4)[2]
                            makenote()
                            say("noted")
                            engine.runAndWait()




                        elif 'WhatsApp'.format(r.recognize_google(audio)) in r.recognize_google(audio): 
                            left = 'WhatsApp'
                            res5 = r.recognize_google(audio)
                            right = "to"
                            msg = res5[res5.index(left)+len(left):res5.index(right)] 
                            friend= r.recognize_google(audio).partition("to")[2]

                            user = os.getlogin()
                            path1 = r"C:\Users"
                            path8 =  str(path1) + "\\"
                            path2 =  str(path8) + str(user)
                            path4 = "\AppData\Local\WhatsApp\WhatsApp.exe"
                            path3 = str(path2) + str(path4)
                            os.startfile(path3)
                            time.sleep (18)
                            pyautogui.hotkey('ctrl', 'f')
                            time.sleep(0.5)
                            pyautogui.write(friend)
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.write(msg) 
                            say ( "whatsapping " + msg + "to" + friend)
                            engine.runAndWait()


                        elif 'simi'.format(r.recognize_google(audio)) in r.recognize_google(audio): 
                            spl_word6 = 'simi'
                            res6 = r.recognize_google(audio).partition(spl_word6)[2]
                            page = requests.get("https://www.google.com/search?q=" +res6)
                            soup = BeautifulSoup( page.content, 'lxml')
                            #print(soup.prettify())
                            results = []

                            for item in soup.find_all( class_="BNeawe s3v9rd AP7Wnd" ):
                                results.append(item.get_text(strip=True))


                            firstthree =  str(results[0:3])
                            print(firstthree)
                            say(firstthree)

                        elif 'timer'.format(r.recognize_google(audio)) in r.recognize_google(audio): 
                            spl_word7 = 'set a timer for'
                            global t
                            t = r.recognize_google(audio).partition(spl_word7)[2]
                            countdown(int(t))

                        
                        elif 'type'.format(r.recognize_google(audio)) in r.recognize_google(audio): 
                            spl_word8 = 'type'
                            what_to_type  = r.recognize_google(audio).partition(spl_word8)[2]
                            time.sleep(0.5)
                            pyautogui.write(what_to_type)


                        elif 'find'.format(r.recognize_google(audio)) in r.recognize_google(audio):
                            spl_word9 = 'find'
                            what_to_find  = r.recognize_google(audio).partition(spl_word9)[2]
                            pyautogui.hotkey('ctrl', 'f')
                            time.sleep(0.5) 
                            pyautogui.write(what_to_find)
                        
                     
                            
                             





                    except:
                        print("error")
                        simi()
                        





root = Tk()

def makenote():  
    threading.Thread(target=simi).start()
    stickynotes1 = StickyNotess(root)
    root.mainloop()
  




simi()






