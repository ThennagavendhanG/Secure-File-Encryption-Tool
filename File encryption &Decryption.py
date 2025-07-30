from cryptography.fernet import Fernet
import os

# Generate a new key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"🔒 File '{filename}' encrypted successfully as '{filename}.enc'.")

# Decrypt a file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    output_file = filename.replace(".enc", "_decrypted")
    with open(output_file, "wb") as file:
        file.write(decrypted)
    print(f"🔓 File '{filename}' decrypted successfully as '{output_file}'.")

# Main menu
def main():
    print("\n--- Secure File Encryption & Decryption Tool ---")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        generate_key()
        print("✅ Key generated and saved as 'secret.key'.")
    elif choice == '2':
        filename = input("Enter the filename to encrypt: ")
        if not os.path.exists(filename):
            print("❌ File not found!")
            return
        key = load_key()
        encrypt_file(filename, key)
    elif choice == '3':
        filename = input("Enter the filename to decrypt (with .enc): ")
        if not os.path.exists(filename):
            print("❌ File not found!")
            return
        key = load_key()
        decrypt_file(filename, key)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
