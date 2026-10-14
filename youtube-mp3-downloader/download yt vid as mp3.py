import youtube_dl, threading ,ttk, time
import tkinter as tk
from tkinter import *



root= tk.Tk()
def get_value_and_start_thread(): #gets value entered and starts main program in seperate thread
    global x1
    x1 = entry1.get()
    threading.Thread(target=tryy).start()

root.title("download any youtube video as mp3") #window title

canvas1 = tk.Canvas(root, width=380, height=150, background='grey',  insertborderwidth=0) #window propertioes
canvas1.pack()

entry1 = tk.Entry(root) #field to enter link
canvas1.create_window(180, 50, window=entry1, width= 280)

label1 = tk.Label(root, text="""enter youtube link 
mp3 will be downloaded at C/users/username or at system path , dont close window""", background='light grey') #disclaimer message
canvas1.create_window(160, 110, window=label1, width=  500) #disclaimer message properties

button = Button(root, text="enter",bg='grey', command=get_value_and_start_thread, font=('new times roman', 12)) #button properties
button.pack(pady=0)

pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=380) #progress bar properties
pb.pack()



def tryy(): #main program 
    try: #check is program can be run / link is enterer properly or any other error is there
        pb.start() #starts progress bar
        video_url = str(x1)
        video_info = youtube_dl.YoutubeDL().extract_info( #mp3 program 
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])


        label3 = tk.Label(root, text="downloaded", font=('helvetica', 12, 'bold'), fg ='green') #displays message downloaded 
        canvas1.create_window(160, 100, window=label3)
        pb.stop() #stops progress bar
        time.sleep(4)
        label3.destroy()#removes label so user can download multiple times 
    
    except: #in case error is raised 
        pb.stop() #stops progress bar 
        label1 = tk.Label(root, text="not entered youtube link or syntax error", font=('helvetica', 12, 'bold'), fg ='red' ) #error message properties 
        canvas1.create_window(180, 100, window=label1)
        time.sleep(4)
        label1.destroy()#removes label so user can try again


root.mainloop()











