from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

salt = get_random_bytes(16)
password = b'this is a seecret'
key_len=16
n=2**14
r=8
p=1

key = scrypt(password , salt ,key_len , n , r ,p)
print(salt)
print("this is the secret: " + str(key))
#salt (string) – A string to use for better protection from dictionary attacks.
# This value does not need to be kept secret, but it should be randomly chosen for each derivation.
# It is recommended to be at least 16 bytes long.

#key_len (integer) – The length in bytes of every derived key.

#N (integer) – CPU/Memory cost parameter. It must be a power of 2 and less than 232

#r (integer) – Block size parameter.

#p (integer) – Parallelization parameter. It must be no greater than (232−1)/(4r)

#num_keys (integer) – The number of keys to derive. Every key is key_len bytes long.
# By default, only 1 key is generated. T


#(2**14 , 8 , 1) for logins (<= 100 ms)
#(2**20 , 8 , 1) for encryption (<=5 s)
