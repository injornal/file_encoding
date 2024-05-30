import os

import pyaes

# key = bytes.fromhex("8e1f3d4831b4f1dee61783bab0e187dee768443a27662a0ef43ad6f375faf14c")
key = os.urandom(32)

with open("key.txt", "w") as f:
    f.write(key.hex())

aes = pyaes.AESModeOfOperationCTR(key)

with open("example.txt", "rb+") as f:
    data = aes.encrypt(f.read())
    f.seek(0)
    f.write(data)

