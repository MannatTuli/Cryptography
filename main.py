from cryptography.fernet import Fernet

key = Fernet.generate_key()

print('Key: ')
print(key)

f = Fernet(key)

token = f.encrypt(b'HERE!') #Enter the string, integer, float to be encrypted here

print('\n')
print('Encrypted: ')
print(token)
print("\n")
print('Decrypted: ')
print(f.decrypt(token))


#Storing keys
file = open('key.key', 'wb')  
file.write(key)  
file.close()

#Call the function to read the key
def key():
	file = open('key.key', 'rb')  
	a = file.read()  
	print('\nKey: ')
	print(a)
	file.close()

key()