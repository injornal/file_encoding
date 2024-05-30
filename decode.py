import sys

import pyaes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# key = bytes.fromhex(sys.argv[1])
# iv = bytes.fromhex(sys.argv[2])
# print(key)

with open("key.txt", "r") as f:
    key = bytes.fromhex(f.read())

# DECRYPTION
# CRT mode decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
with open("example.txt", "rb+") as f:
    decrypted = aes.decrypt(f.read()).decode('utf-8')

with open("example.txt", "r+") as f:
    f.seek(0)
    f.write(decrypted)

