# Caesar Cipher Encryption & Decryption

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Encrypt or Decrypt? ").lower()

    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")
