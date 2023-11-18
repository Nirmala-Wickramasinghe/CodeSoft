import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    try:
        # Get the desired length of the password from the user
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Invalid password length. Please enter a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    password_generator()
