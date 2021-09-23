import time
import tkinter as tk

import win32api

import tts
from multiprocessing import Process
import keyboard

from comb import comb
from trans import trans_from_baidu

myTTS = tts.TTS(250)


def run_TTS():
    while True:
        if keyboard.is_pressed('ctrl+q'):
            myTTS.text_to_speech(myTTS.copy_clipboard())
        if keyboard.is_pressed('q'):
            break


def create_window(paragraph):
    combed_paragraph = comb(paragraph)
    print(combed_paragraph)
    translated_paragraph = trans_from_baidu(combed_paragraph)
    posx, posy = win32api.GetCursorPos()
    window = tk.Tk()
    window.title('银的宝典')
    window.geometry(f"500x200+{posx}+{posy}")
    label = tk.Label(window, text=translated_paragraph, padx=10, pady=10, wraplength=500)
    label.pack()
    window.mainloop()


def show_word():
    while True:
        if keyboard.is_pressed('ctrl+q'):
            paragraph = myTTS.copy_clipboard()
            print(paragraph)
            create_window(paragraph)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.instruct = tk.Text(self, height=10, width=30)
        instructions = """Highlight text and press r"""
        self.instruct.pack(side="top")
        self.instruct.insert(tk.END, instructions)
        self.read = tk.Button(self)
        self.read["text"] = "read"
        self.read["command"] = self.run_tts()
        self.read.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_new_window(self):
        sub = tk.Tk()
        sub.title('Hello world')

    def run_tts(self):
        process = Process(target=run_TTS)
        process.start()

    def run_trans(self):
        paragraph = """Rust is also a statically typed language, meaning that a variable can never change its type, like from a number to a string. If you’re coming from languages like C/C++ or Java, this will be familiar because those languages are also statically typed. You don’t always have to declare a variable’s type in Rust because the compiler can often figure it out from the context, but the variable is still never allowed to change its type.
        """
        trans_from_baidu(paragraph)


if __name__=='__main__':
    show_word()
    # run_TTS()
    # root = tk.Tk()
    # root.title('InstaRead')
    # app = Application(master=root)
    # app.mainloop()