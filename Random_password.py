import random
import string

length = 8   # password length

password = ""
for i in range(length):
    password += random.choice(string.ascii_letters + string.digits)

print("Generated Password:", password)