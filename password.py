import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 1:
        return "Password length should be at least 1"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")