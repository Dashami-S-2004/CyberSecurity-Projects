# Image Encryption & Decryption using Pixel Manipulation
from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j][:3]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    img.save(output_path)
    print("Image encrypted and saved as", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j][:3]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    img.save(output_path)
    print("Image decrypted and saved as", output_path)


if __name__ == "__main__":
    choice = input("Encrypt or Decrypt? ").lower()
    key = int(input("Enter key (number): "))
    input_file = input("Enter input image path: ")
    output_file = input("Enter output image path: ")

    if choice == "encrypt":
        encrypt_image(input_file, output_file, key)
    else:
        decrypt_image(input_file, output_file, key)
