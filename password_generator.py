#A password generator
import random 
print("Welcome To Your password Generator")

print("===========================")
print(f"Your passwords are below:")
print()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_,./0123456789"

def password_generator(number_of_password, length_of_password):
    for num in range(number_of_password):
        password = ""
        for length in range(length_of_password):
            password += random.choice(chars)
        print(password)

password_generator(5, 9)