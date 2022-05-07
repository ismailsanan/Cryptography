from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad

def shortkey8_enc(key, message, iv):
    actual_key = bytes.fromhex(key)*16
    cipher = AES.new(actual_key, AES.MODE_CBC , iv)
    return cipher.encrypt(pad(message , AES.block_size))

def shortkey8_dec ( key , message , iv):
    actual_key = bytes.fromhex(key) * 16
    cipher = AES.new(actual_key, AES.MODE_CBC, iv)
    return cipher.decrypt(message)


def double8_enc (key1,key2, message , iv):
    actual_key1 = bytes.fromhex(key1)*16
    actual_key2 = bytes.fromhex(key1) * 16
    cipher1 = AES.new(actual_key1, AES.MODE_CBC, iv)
    cipher2= AES.new(actual_key2, AES.MODE_CBC, iv)
    return cipher1.encrypt(cipher2.encrypt(pad(message, AES.block_size)))


if __name__ == '__main__':
    key1 = format(randint(0,256), '02x')
    key2= format(randint(0,256), '02x')

    print(key1)
    print(key1)

    iv = get_random_bytes(16)
    #print(iv)

    plaintext = b'this is a meaningless messg'
    ciphetext = double8_enc(key1 , key2 , plaintext , iv)
    NUM_KEYS = 256

    dict = {}
    for i in range(0,NUM_KEYS):
        dict[shortkey8_enc(format(i , '02x'),plaintext , iv)] = i
    for  i in range(0,NUM_KEYS):
        intermediate_artifate = shortkey8_dec(format(i , '02x') ,ciphetext , iv)
        if intermediate_artifate in dict.keys():
            print("k1 = " , end= ' ')
            print(dict.get(intermediate_artifate))
            print("k2 = " + str(i))