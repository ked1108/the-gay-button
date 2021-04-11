#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import time
import pyautogui

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.thats_gay = ttk.Button(self)
        self.thats_gay["text"] = "That's A Bit Gay"
        self.thats_gay["command"] = self.say_gay
        self.thats_gay.pack(side="top", pady=20)

        self.quit = ttk.Button(self, text="exit", 
                              command=self.master.destroy)
        self.quit.pack(side="bottom", pady=20)

    def say_gay(self):
        time.sleep(3)
        pyautogui.typewrite("that's a bit gay")
        

root = tk.Tk()
app = Application(master=root)
root.title("That's a bit gay")
root.geometry("250x175")
app.mainloop()