from hashlib import sha256

message = b"hello world"
h = sha256()
h.update(message)
print(h.hexdigest())
