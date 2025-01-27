def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

# Example usage:
encrypted = caesar_cipher("Hello, World!", 3, 'encrypt')
print(encrypted)  # Output: "Khoor, Zruog!"
decrypted = caesar_cipher(encrypted, 3, 'decrypt')
print(decrypted)  # Output: "Hello, World!"
