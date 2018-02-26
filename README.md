# What is KeyOwl?
KeyOwl is a keylogger. Which means that it records everything typed by the user of the device it runs on.
It runs on startup (if everything goes right) and sends you all the data using Gmail.

# What does it do exactly?
Once KeyOwl runs for the first time it creates a startup shortcut of itself and then a log.txt file where it will store all 
the keystrokes that it records.

Every time KeyOwl is run, it will encode the content of the log.txt file to Base64 and send it to you via e-mail.
In order to read the contents you can use a simple decoder. KeyOwl encodes the contents of the log.txt file to prevent different problems that might arise from a few recorded characters.

### Disclaimer! ###

This is made for educational purposes only! I do not condone malicious use of this script! I am also not responsible for the actions
of anyone using this script!

