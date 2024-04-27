import random
letters = "qwertyuiopasdfghjklzxcvbnm"
caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
combined = letters + caps + numbers
password = ""
password = random.choice(combined)

for _ in range(8):
    password += random.choice(combined)
    
print(password)

