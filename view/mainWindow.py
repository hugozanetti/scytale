from tkinter import *
#Bizarro após o import acima ser necessario importar novamente para funcionar o programa!
from tkinter import messagebox
from tkinter.scrolledtext import *
#Estudar sobre o pacote ttk, parece que ele implementa uma classe Frame também e que não 
#suporta o parâmetro pady
from tkinter.ttk import Combobox
# from controller.ctrl.CtrlKey import generate NÃO FUNCIONOU!
from controller.ctrl import CtrlKey


class MainWindow(Tk):
    
     def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
     def validateEncrypting(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText, txtMsg:ScrolledText, txtEncriptedMsg:ScrolledText,  comboAction:Combobox):
         
         if comboAction.get() == '':
             messagebox.showinfo('Validação',  'Escolha alguma ação através do combobox!')
             comboAction.focus()
             return True
         else:
             if comboAction.get() == 'Encrypt':
                 if txtMsg.get('1.0', 'end-1c') == '':
                     messagebox.showinfo('Validação',  'Para criptografar é necessario preencher o campo "Message"!')
                     txtMsg.focus()
                     return True
                 CtrlKey.encryptRun(self,  txtPrivKey, txtPubKey, txtMsg, txtEncriptedMsg, comboAction)
                 return True
             else: # Action = 'Decrypt'
                 if txtEncriptedMsg.get('1.0', 'end-1c') == '':
                     messagebox.showinfo('Validação',  'Para descriptografar é necessario o campo "Encrypted message"!')
                     txtEncriptedMsg.focus()
                     return True 
                 CtrlKey.encryptRun(self,  txtPrivKey, txtPubKey, txtMsg, txtEncriptedMsg, comboAction)
                 return True
                  
        
    
     def clean(self,  txtArea1:ScrolledText ,  txtArea2:ScrolledText):
         txtArea1.delete('1.0',  END)
         txtArea2.delete('1.0',  END)
        
        
        
     def initUI(self):
        self.title('Scytale')
        #self.style = Style()
        #self.style.theme_use('default')
        
        #Início do frame de geração das chaves
        frameGenKeys = Frame(self,  relief=RAISED,  pady=10,  borderwidth=2)
        
        lbl = Label(frameGenKeys, text='Private Key:')
        lbl.grid(column=0, row=0,  sticky=W)
        
        txtAreaPrivateK = ScrolledText(frameGenKeys, width=40, height=6)
        txtAreaPrivateK.grid(column=0, row=1)
        
        lbl = Label(frameGenKeys, text='Public Key:')
        lbl.grid(row=0, column=1,  sticky=W)
        
        txtAreaPublicK = ScrolledText(frameGenKeys, width=40, height=6)
        txtAreaPublicK.grid(column=1, row=1)
        
        btnKeyGen = Button(frameGenKeys, text='Generate Keys',  height=2,  command=lambda:CtrlKey.generate(self,  txtAreaPrivateK, txtAreaPublicK))
        btnKeyGen.grid(row=2,  column=0,  pady=10)                
        btnCleanKey = Button(frameGenKeys, text='Clean keys',  height=2,  command=lambda:self.clean(txtAreaPrivateK, txtAreaPublicK))
        btnCleanKey.grid(row=2,  column=1,  pady=10)
        
        frameGenKeys.pack(fill=X)
        #Fim do frame de geração das chaves
        
        
        
        #Início do frame Encrypting 
        frameEncrypting = Frame(self,  relief=RAISED, pady=10,  borderwidth=2)
        
        lbl = Label(frameEncrypting, text='Encrypted message:')
        lbl.grid(row=0,  column=0,  sticky=W)
        lbl = Label(frameEncrypting, text='Message:')
        lbl.grid(row=0,  column=1,  sticky=W)
        
        txtAreaMsgEncoded = ScrolledText(frameEncrypting, width=40, height=6)
        txtAreaMsgEncoded.grid(row=1, column=0)
        txtAreaMsg = ScrolledText(frameEncrypting, width=40, height=6)
        txtAreaMsg.grid(row=1, column=1)
        
        lbl = Label(frameEncrypting, text='Action:')
        lbl.grid(row=2,  column=0,  sticky=W)
        combo = Combobox(frameEncrypting)
        combo['values']= ('Encrypt', 'Decrypt')
        #combo.current(1) set the selected item 
        combo.grid(row=2,  column=0, padx=20, sticky=E)        
       
        btnEncryptMsg = Button(frameEncrypting, text='Run',  width=10,  height=2,  command=lambda:self.validateEncrypting(txtAreaPrivateK, txtAreaPublicK, txtAreaMsg, txtAreaMsgEncoded, combo))
        btnEncryptMsg.grid(row=2,  column=1,  pady=10, padx=10, sticky=W)
        btnCleanMsg = Button(frameEncrypting, text='Clean messages',  height=2,  command=lambda:self.clean(txtAreaMsgEncoded, txtAreaMsg))
        btnCleanMsg.grid(row=2,  column=1,  pady=10, padx=15, sticky=E)
        
        
        
        frameEncrypting.pack(fill=X)
        #Fim do frame Encrypting 
        
   
