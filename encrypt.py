import cryptography	
from cryptography.fernet import Fernet

#Generating the key
key = Fernet.generate_key()

#Saving the key in .key format
file = open('key.key', 'wb')
file.write(key) # The key is of type bytes
file.close()

#Taking the input of username and password for encoding
username=input('Enter username ')
password=input('Enter password ')

#Printing the key
print('\nKey: '+ str(key))

#Converting the string into bytes
username=username.encode()
password=password.encode()

f = Fernet(key)

#Encrypting the username and password
username_encrypted=f.encrypt(username)
password_encrypted=f.encrypt(password)

print('\nEncrypted Username: '+ str(username_encrypted))
print('\nEncrypted Password: '+ str(password_encrypted))

#Decrypting the username and password
username_decrypt=f.decrypt(username_encrypted)
password_decrypt=f.decrypt(password_encrypted)

#Printing the Decrypted username and password
print('\nDecrypted Username: '+ str(username_decrypt))
print('Decrypted Password: '+ str(password_decrypt))
