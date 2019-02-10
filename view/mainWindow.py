from tkinter import *

class MainWindow(Tk):
     def __init__(self):
        super().__init__()
        
        self.initUI()
        
     def initUI(self):
        frameGenKeys = Frame(self,  relief=RAISED,  borderwidth=1)
        btnKeyGen = Button(frameGenKeys, text='Generate Keys')
        btnKeyGen.grid(row=0, column=0)
        frameGenKeys.pack(fill=X)
