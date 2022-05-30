from tkinter import *

class ChildWindow:
    def __init__(self, parent, width, height, title='MyWindow', resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+300+100')
        self.root.resizable(resizable[0], resizable[1])

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()