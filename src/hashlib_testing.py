import hashlib

h = hashlib.new('sha256')
h.update(b'The fitness gram pacer test is a multi stage aerobic capacity test')
h.hexdigest()
print(h.digest_size())