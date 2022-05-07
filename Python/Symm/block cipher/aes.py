from pydoc import plain

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad , unpad
import base64

key = get_random_bytes(32)


cipher = AES.new(key= key, mode=AES.MODE_CBC)
iv = cipher.iv

plaintext = b'this is my aes'

ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))

print(ciphertext)

#decrypt

cipherdec = AES.new(key= key, mode=AES.MODE_CBC,iv=iv)

decrypted = unpad(cipherdec.decrypt(ciphertext) , AES.block_size)

print(decrypted)


data = b'ciao'

base64_en = base64.b64encode(data)

print(base64_en)

base64_de = base64.b64decode(base64_en)
print(base64_de)
