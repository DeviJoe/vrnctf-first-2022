import base64
from Cryptodome.Cipher import AES
from Cryptodome import Random
import hashlib

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw).encode('utf8')
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ans = cipher.encrypt(raw)
        return base64.b64encode(iv + self.key + ans)

    def decrypt(self, enc):
        # hidden
        pass


secret_16_bytes = "b'****************"

gen_key = hashlib.sha256(secret_16_bytes).digest()

aes = AESCipher(gen_key)

text = "****************************"
print(aes.encrypt(text))
