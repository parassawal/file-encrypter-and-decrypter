from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a key and save it to a file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

def load_key():
    """Load the key from the 'key.key' file."""
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    """Encrypt the contents of a file."""
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        print(f"File '{file_path}' has been encrypted.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_file(file_path):
    """Decrypt the contents of a file."""
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        print(f"File '{file_path}' has been decrypted.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main():
    while True:
        print("\nFile Encryption/Decryption Application")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_path = input("Enter the path of the file to encrypt: ")
            encrypt_file(file_path)
        elif choice == "3":
            file_path = input("Enter the path of the file to decrypt: ")
            decrypt_file(file_path)
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
