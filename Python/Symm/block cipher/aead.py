from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64 , json


#sym enc object aead
################################
#sender


key = get_random_bytes(32)
msg = b'this is a secret'
head = b'auth only msg'


cipher = AES.new(key=key, mode=AES.MODE_GCM)
cipher.update(head)
ciphertext,tag = cipher.encrypt_and_digest(msg)
keys=['tag', 'ciphertext', 'head', 'nonce']
data = [base64.b64encode(x).decode() for x in (tag,ciphertext,head,cipher.nonce)]

#print(type(base64.b64encode(head).decode())) #changes the class type with decode string without bytes

packed_data = json.dumps(dict(zip(keys,data)))
print(packed_data)

#############################################
#reciever
unpacked_data = json.loads(packed_data)
print(unpacked_data)


cipher_ver = AES.new(key , AES.MODE_GCM , nonce = base64.b64decode(unpacked_data["nonce"]))
cipher_ver.update(base64.b64decode(unpacked_data["head"]))
try:
    plaintext = cipher_ver.decrypt_and_verify(base64.b64decode(unpacked_data["ciphertext"]),base64.b64decode(unpacked_data["tag"]))
except ValueError:
    print("something went wrong")


print(plaintext)