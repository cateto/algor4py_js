import hashlib

m = hashlib.sha256()
m.update('1234'.encode('utf-8'))

with open('passwd.txt', 'w') as f:
    f.write(m.hexdigest())