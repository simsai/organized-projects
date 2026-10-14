from msilib.schema import Icon
import speech_recognition as sr
import win32gui, win32con, win32process , time 
from plyer import notification



notification.notify(
    title = 'appliocation started',
    message = 'application started but hidden, to stop script say stop then end from task manager or just leave it u will get not perfomance issues',
    app_icon = None,
    timeout = 10,
)


r = sr.Recognizer()
i = 1
while i < 6:

    time.sleep(1)

    hide = win32gui.GetForegroundWindow()

    with sr.Microphone() as source:
      
        
        audio = r.listen(source)

      
        text = r.recognize_google(audio)
        
        notification.notify(
            title = 'unclear',
            message = text,
            app_icon = None,
            timeout = 10,
        )

        

    if text == "hello":
        win32gui.ShowWindow( hide , win32con.SW_FORCEMINIMIZE)

    elif text == "stop":
        notification.notify(
        title = 'stopped',
        message = 'application stopped',
        app_icon = None,
        timeout = 10,
    )
        break