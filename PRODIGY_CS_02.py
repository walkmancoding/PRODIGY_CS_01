from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

def main():
    print("Welcome to the Image Encryption Tool!")
    choice = input("Would you like to encrypt or decrypt an image? (e/d): ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        return

    input_image_path = input("Enter the path to the input image: ").strip()
    output_image_path = input("Enter the path to save the output image: ").strip()
    try:
        key = int(input("Enter the encryption/decryption key (an integer): ").strip())
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return
    
    if choice == 'e':
        encrypt_image(input_image_path, output_image_path, key)
    else:
        decrypt_image(input_image_path, output_image_path, key)

if __name__ == "__main__":
    main()
