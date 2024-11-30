import hashlib

sec_key = 'ckczppom'
seed = 1

while True:
    key = sec_key + str(seed)
    md5hash = hashlib.md5(key.encode())
    if md5hash.hexdigest().startswith('00000'):
        break
    seed += 1
print(seed)