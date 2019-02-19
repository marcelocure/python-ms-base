import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from config import crypt_key

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]

def iv():
    """
    The initialization vector to use for encryption or decryption.
    It is ignored for MODE_ECB and MODE_CTR.
    """
    return chr(0) * 16

class AESCipher(object):

    def __init__(self):
        self.key = crypt_key

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')