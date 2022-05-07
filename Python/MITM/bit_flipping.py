from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
print( "key= ", key, "nonce= ")
cipher = ChaCha20.new(key = key)

plaintext = b'we need to change this number 100$'

ciphertext = cipher.encrypt(plaintext)

print(plaintext)
print(ciphertext)


############### attacker #############

index = plaintext.index(b'1')
#print(index)

ciphertext_array = bytearray(ciphertext)
#print(ciphertext_array[index])

new_byte = '9'
#print(ord(new_byte)) #ascii code for 9

#print(plaintext[index] ^ ord(new_byte))

ciphertext_array[index] = ciphertext[index] ^ plaintext[index] ^ ord(new_byte)

print(ciphertext_array)


cipher_dec = ChaCha20.new(key = key ,  nonce= cipher.nonce)
ciphertext_dec = cipher_dec.decrypt(ciphertext_array)
print(ciphertext_dec)