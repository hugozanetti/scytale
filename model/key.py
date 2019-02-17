from tkinter import *
from tkinter.scrolledtext import *
from tkinter.ttk import Combobox
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
import binascii
import ast

class Key:

    def privKey(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText):
        random_gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        
        visibleKey = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
        secretKey = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
        

        # Grava todas as chaves geradas pelo algorito RSA em um arquivo de texto
        with open("C:/Python/scytale/data/keysfile.txt", "a+") as f:
            #read_data = f.read()
            """
            O arquivo é inteiramente gravado com a primeira linha contendo uma privatekey e
            a segunda linha contendo a correspondente publickey, portanto sempre a última linha
            conterá uma PUBLICKEY e a linha anterior a sua geradora(PRIVATEKEY)
            """
            record = str(secretKey) + "\n" + str(visibleKey) + "\n"   
            f.write(record)

            f.close()

        # Exibe o resultado na GUI
        txtPrivKey.insert(INSERT, secretKey)
        txtPubKey.insert(INSERT, visibleKey)
        
        
     
    def encrypting(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText, txtMsg:ScrolledText, txtEncriptedMsg:ScrolledText,  comboAction:Combobox):
         strAction = comboAction.get()
         chavePreenchida = False
         if strAction == 'Encrypt':  
             if txtPubKey.get('1.0', 'end-1c') != '':
                 chavePreenchida = True
                 cryptKey = PKCS1_OAEP.new(RSA.importKey(binascii.unhexlify(txtPubKey.get('1.0', 'end-1c'))))             
         else: # Decrypt
             if txtPrivKey.get('1.0', 'end-1c') != '':
                 chavePreenchida = True
                 cryptKey = PKCS1_OAEP.new(RSA.importKey(binascii.unhexlify(txtPrivKey.get('1.0', 'end-1c'))))
         
         
         if not chavePreenchida:
             f = open("C:/Python/scytale/data/keysfile.txt", "r")
             file_lines = f.readlines()
             f.close()
             
             if strAction == 'Encrypt':
                 subtracao = 1 #public key
             else:
                 subtracao = 2 #private key
                 
                 
             last_line = file_lines[len(file_lines)-subtracao] #last_line é chave que será usada na operação de criptografia!
             cryptKey = PKCS1_OAEP.new(RSA.importKey(binascii.unhexlify(last_line.strip())))
             
             
         if strAction == 'Encrypt':
             b = bytes(str(txtMsg.get('1.0', 'end-1c')), "utf-8")
             encrypted = cryptKey.encrypt(b)
             #conversão (str) para jogar essa informação na caixa de texto da GUI !
             txtEncriptedMsg.insert(INSERT, binascii.hexlify(encrypted).decode('ascii')) 
         else:
             decrypted = cryptKey.decrypt(binascii.unhexlify(txtEncriptedMsg.get('1.0', 'end-1c')))
             txtMsg.insert(INSERT, str(decrypted.decode()))
                 
