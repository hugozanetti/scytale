from tkinter import *
from tkinter.scrolledtext import *

class MainWindow(Tk):
     def __init__(self):
        super().__init__()
        
        self.initUI()
        
     def initUI(self):
        frameGenKeys = Frame(self,  relief=RAISED,  borderwidth=1)
        lbl = Label(frameGenKeys, text='Private Key:')
        lbl.grid(column=0, row=0)
        
        txtAreaPrivateK = ScrolledText(frameGenKeys, width=40, height=10)
        txtAreaPrivateK.grid(column=0, row=1)
        
        lbl = Label(frameGenKeys, text='Public Key:')
        lbl.grid(column=1, row=0)
        
        txtAreaPublicK = ScrolledText(frameGenKeys, width=40, height=10)
        txtAreaPublicK.grid(column=1, row=1)
        
        btnKeyGen = Button(frameGenKeys, text='Generate Keys')
        btnKeyGen.grid(column=0, row=2)
        frameGenKeys.pack(fill=X)
