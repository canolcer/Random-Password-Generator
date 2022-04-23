import random
import string

numbers = string.digits
punctuation = string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase
total = numbers + punctuation + upper + lower


password = ""
length = random.randint(8, 64)
i = 0
while i < length:
    index = random.randint(0, len(total) - 1)
    if not (total[index].lower() in password):
        password += total[index]
        i += 1
print(password)
