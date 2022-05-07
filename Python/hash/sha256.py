import hashlib


plaintext = b"this is the secret"

hash = hashlib.sha256(plaintext).digest()
print(hash)

hash2 = hashlib.sha256()
hash2.update(plaintext)
result = hash2.digest()
print(hash2.block_size)
print(hash2.digest_size)
print(result)

obj = hashlib.new('sha256') # hashlib const
obj.update(plaintext)
print(obj.hexdigest())
print(obj.digest())
