def encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with the given shift."""
    encrypted_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, leave it as is
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with the given shift."""
    decrypted_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # If it's not a letter, leave it as is
        else:
            decrypted_text += char
    return decrypted_text


def main():
    print("Caesar Cipher Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        text = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        encrypted_message = encrypt(text, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice == '2':
        text = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        decrypted_message = decrypt(text, shift)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
