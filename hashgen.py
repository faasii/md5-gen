import hashlib

#author: faasi
#https://github.com/faasii/

str = input("Enter Plain text : ")
result = hashlib.md5(str.encode())

hash = result.hexdigest()

print(hash)

