from tkinter.scrolledtext import *
from model.key import Key

class CtrlKey:
    
    def generate(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText):
        Key.privKey(txtPrivKey, txtPubKey)
