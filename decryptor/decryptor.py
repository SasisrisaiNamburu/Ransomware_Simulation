from cryptography.fernet import Fernet
import os

# Load the AES encryption key
def load_key():
    return open("../key.key", "rb").read()

# Decrypt all .locked files
def decrypt_files():
    folder = "../test_files/"
    key = load_key()
    fernet = Fernet(key)

    for filename in os.listdir(folder):
        if not filename.endswith(".locked"):
            continue

        file_path = os.path.join(folder, filename)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        # Remove .locked extension
        original_path = file_path.replace(".locked", "")

        with open(original_path, "wb") as file:
            file.write(decrypted_data)

        os.remove(file_path)

    print("Decryption complete. Files restored!")

decrypt_files()
