from tkinter import *
from child_window import ChildWindow

class Window:
    def __init__(self, width, height, title='MyWindow', resizable=(False, False), icon='resources/icon.ico'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(resizable[0], resizable[1])

        self.label = Label(self.root, text='This is a label', bg='#e0e009')
        #self.face_image = PhotoImage(file=r'resources/people.png')
        #self.label = Label(self.root, image=self.face_image)
        #self.label.image = self.face_image


    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack()

    def create_child(self, width, height, title='Child', resizable=(False, False)):
        ChildWindow(self.root, width, height, title, resizable)

if __name__ == '__main__':
    window = Window(800, 400, 'TKINTER')
    #window.create_child(400, 200)
    window.run()