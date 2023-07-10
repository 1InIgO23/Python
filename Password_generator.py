import secrets
import string

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation
alphabet = letters + numbers + special

lenght = int(input("Enter the password length: "))

password = ""
for i in range(lenght):
    password += "".join(secrets.choice(alphabet))
print(password)