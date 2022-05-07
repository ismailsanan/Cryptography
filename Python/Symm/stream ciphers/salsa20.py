from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
nonce = get_random_bytes(8)
cipher = Salsa20.new(key= key , nonce = nonce)

plaintext = b'this is my first crypto'

ciphertext = cipher.encrypt(plaintext)

print("plaintext: " + str(plaintext))

print("ciphertext: " + str(ciphertext))

## decryption we need another object why

cipherdec = Salsa20.new(key=key , nonce = nonce)
decryptText = cipherdec.decrypt(ciphertext)

print("decrpyed: " + str(decryptText))