
import base64
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
data = b'this is a secret'
key = get_random_bytes(32)
hmac = HMAC.new(key=key,digestmod=SHA256)
mac = hmac.update(data).digest()


data2 = b'this another secret'
hmac2 = HMAC.new(key=key,digestmod=SHA256)
mac2 = hmac2.update(data2).digest()

hmac_ver = HMAC.new(key =key,digestmod=SHA256)
hmac_ver.update(b64["message"].encode("utf-8"))

if hmac_ver.verify(mac, mac2):
    print("verrified")

else:
    print("unverified")


