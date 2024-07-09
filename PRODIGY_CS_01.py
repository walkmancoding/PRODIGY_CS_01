def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 - shift_amount) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        return

    message = input("Enter your message: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    if choice == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
