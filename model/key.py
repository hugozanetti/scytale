from tkinter.scrolledtext import *

class Key:

    def privKey(self, txtPrivKey:ScrolledText, txtPubKey:ScrolledText):
        random_gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        
        #visibleKey = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
        #secretKey = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')

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
        txtPrivKey.insert(INSERT, private_key.exportKey(format='DER'))
        txtPubKey.insert(INSERT, public_key.exportKey(format='DER'))
        
