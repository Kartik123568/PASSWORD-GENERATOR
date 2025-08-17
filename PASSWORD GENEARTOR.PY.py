import random
import string


def generate_password(length):
    if length < 4:
        return "❌ Password length too short!"

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    print("🔐 Random Password Generator")
    try:
        length = int(input("Enter password length (min 4): "))
        pwd = generate_password(length)
        print(f"Generated Password: {pwd}")
    except ValueError:
        print("❌ Invalid input. Enter a number.")


main()
