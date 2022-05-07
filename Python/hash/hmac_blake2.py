from hashlib import blake2b
import pwn


from Crypto.Random import get_random_bytes

key = get_random_bytes(32)


text = b"this is a secret"

hash = blake2b(key , digest_size=16 )
hash.update(text)
hash.update(b"hellowz")
print(hash.digest())

print(hash.hexdigest())
