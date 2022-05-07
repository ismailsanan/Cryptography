from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
nonce = get_random_bytes(8)

cipher = ChaCha20.new(key=key , nonce=nonce )

plaintext = b'this is chacha20 try'


ciphertext = cipher.encrypt(plaintext)

print(ciphertext)

#decrypt

decCipher = ChaCha20.new(key=key,nonce = nonce )

decText = decCipher.decrypt(ciphertext)

print(decText)