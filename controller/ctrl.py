from tkinter.scrolledtext import *
from tkinter.ttk import Combobox
from model.key import Key

class CtrlKey:
    
    def generate(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText):
        Key.privKey(self,  txtPrivKey, txtPubKey)
        
    def encryptRun(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText, txtMsg:ScrolledText, txtEncriptedMsg:ScrolledText,  comboAction:Combobox):
         Key.encrypting(self, txtPrivKey, txtPubKey,  txtMsg,  txtEncriptedMsg,  comboAction)
        
    """"
    def cript(self, txtPubKey:ScrolledText,  txtMsg:ScrolledText,  txtMsgEncoded:ScrolledText):
        Key.criptMessage(self, txtPubKey, txtMsg,  txtMsgEncoded)
        
        
    def deCript(self, txtPrivKey:ScrolledText,  txtMsg:ScrolledText,  txtMsgEncoded:ScrolledText):
        Key.deCriptMessage(self, txtPrivKey, txtMsg,  txtMsgEncoded)
    """
