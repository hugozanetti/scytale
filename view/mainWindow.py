from tkinter import *
from tkinter.scrolledtext import *
from controller.ctrl.CtrlKey import generate


class MainWindow(Tk):
    
     def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
        
     def initUI(self):
        self.title('Scytale')
        #self.style = Style()
        #self.style.theme_use('default')
        
        frameGenKeys = Frame(self,  relief=RAISED,  pady=10,  borderwidth=2)
        
        lbl = Label(frameGenKeys, text='Private Key:')
        lbl.grid(column=0, row=0,  sticky=W)
        
        txtAreaPrivateK = ScrolledText(frameGenKeys, width=40, height=6)
        txtAreaPrivateK.grid(column=0, row=1)
        
        lbl = Label(frameGenKeys, text='Public Key:')
        lbl.grid(row=0, column=1,  sticky=W)
        
        txtAreaPublicK = ScrolledText(frameGenKeys, width=40, height=6)
        txtAreaPublicK.grid(column=1, row=1)
        
        btnKeyGen = Button(frameGenKeys, text='Generate Keys',  height=2,  command=generate(txtAreaPrivateK, txtAreaPublicK))
        btnKeyGen.grid(row=2,  column=0,  pady=10)                
        btnKeyGen = Button(frameGenKeys, text='Clean keys',  height=2)
        btnKeyGen.grid(row=2,  column=1,  pady=10)
        
        frameGenKeys.pack(fill=X)
        
        
        frameEncript = Frame(self,  relief=RAISED, pady=10,  borderwidth=2)
        
        lbl = Label(frameEncript, text='Encoded text:')
        lbl.grid(row=0,  column=0,  sticky=W)
        lbl = Label(frameEncript, text='Text to encode:')
        lbl.grid(row=0,  column=1,  sticky=W)
        
        txtAreaMsgEncoded = ScrolledText(frameEncript, width=40, height=6)
        txtAreaMsgEncoded.grid(row=1, column=0)
        txtAreaMsg = ScrolledText(frameEncript, width=40, height=6)
        txtAreaMsg.grid(row=1, column=1)
        
        btnEncryptMsg = Button(frameEncript, text='Encript Message',  height=2)
        btnEncryptMsg.grid(row=2,  column=0,  pady=10)
        btnCleanMsg = Button(frameEncript, text='Clean messages',  height=2)
        btnCleanMsg.grid(row=2,  column=1,  pady=10)        
        
        
        frameEncript.pack(fill=X)
        
        
        
        frameDecript = Frame(self,  relief=RAISED, pady=10,  borderwidth=2)
        
        lbl = Label(frameDecript, text='Encripted message:')
        lbl.grid(row=0,  column=0,  sticky=W)
        lbl = Label(frameDecript, text='Decripted message:')
        lbl.grid(row=0,  column=1,  sticky=W)
        
        txtAreaCriptedMsg = ScrolledText(frameDecript, width=40, height=6)
        txtAreaCriptedMsg.grid(row=1, column=0)
        txtAreaDecriptedMsg = ScrolledText(frameDecript, width=40, height=6)
        txtAreaDecriptedMsg.grid(row=1, column=1)
        
        btnDecriptMsg = Button(frameDecript, text='Decript Message',  height=2)
        btnDecriptMsg.grid(row=2,  column=0,  pady=10)
        btnCleanMsg2 = Button(frameDecript, text='Clean messages',  height=2)
        btnCleanMsg2.grid(row=2,  column=1,  pady=10)        
        
        
        frameDecript.pack(fill=X)
