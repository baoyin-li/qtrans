import os
import time

import pyautogui as pya
import pyperclip
import pyttsx3

class TTS(object):
    def __init__(self,speed):
        self.engine = pyttsx3.init()

        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate',speed)

    def text_to_speech(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def copy_clipboard(self):
        pya.hotkey('ctrl', 'c')
        time.sleep(.10)                     #wait for copy function
        return pyperclip.paste()