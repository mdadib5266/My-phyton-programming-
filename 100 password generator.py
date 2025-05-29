import random
import string
password = []
random1 = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+'
#random = range(0,47)
while True:
    key = random1[random.randint(0,73)]
    password.append(key)
    if len(set(password))==8:
        break
print(password)

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))
print(''.join(set(password)),len(set(password)))
print(generate_password(12),len(generate_password(12)))
#print(random.randint(1,10))