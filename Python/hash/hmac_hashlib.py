import hmac
import hashlib
from Crypto.Random import get_random_bytes
key = get_random_bytes(32)
msg = b'this is a secret'
msg2 = b'this is a secret'

mac = hmac.new(key=key , digestmod= hashlib.sha256)
mac.update(msg)
hmac_digest = mac.digest()

mac2 = hmac.new(key=key  , digestmod=hashlib.sha256)
mac2.update(msg2)
hmac_digest2 = mac2.digest()

if hmac.compare_digest(hmac_digest,hmac_digest2):
    print("Verrified")

else:
    print("UnVerrified")


