import base64

from Cryptodome import Random
from Cryptodome.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw).encode('utf8')
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ans = cipher.encrypt(raw)
        return base64.b64encode(iv + self.key + ans)


def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    key = enc[16:48]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[48:]).decode('utf8'))


text = b'H8Kl7L8s6YxEtgKmdhOq25+ICevOW2I/T1jKMvHz8D6F7hpBgZ0BoTxiLIsMqyyVuzWMpjfQxdP3cJbkyhO6Q3gvmzW8uupnvH8NibgJHiZNXnvsKmiLxuMduP8wkCwP=='
print(decrypt(text))
