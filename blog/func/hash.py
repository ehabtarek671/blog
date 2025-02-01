import hashlib

def md5hash(text):
    return hashlib.md5(text.encode()).hexdigest()