# ==============================
# 1️⃣ CAESAR CIPHER
# ==============================

def caesar_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Caesar Cipher"""
    result = ""
    for char in plaintext:
        if char.isalpha():  # hanya huruf yang dienkripsi
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # karakter non-huruf tidak berubah
    return result


def caesar_decrypt(ciphertext, key):
    """Mendekripsi teks Caesar Cipher"""
    return caesar_encrypt(ciphertext, -key)


# --- Contoh Uji Caesar Cipher ---
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)

print("=== CAESAR CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
print()


# ==============================
# 2️⃣ VIGENÈRE CIPHER
# ==============================

def vigenere_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Vigenère Cipher"""
    result = []
    key = key.lower()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def vigenere_decrypt(ciphertext, key):
    """Mendekripsi teks Vigenère Cipher"""
    result = []
    key = key.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


# --- Contoh Uji Vigenère Cipher ---
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)

print("=== VIGENÈRE CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
print()


# ==============================
# 3️⃣ TRANSPOSITION CIPHER
# ==============================

def transpose_encrypt(plaintext, key=5):
    """Mengenkripsi teks menggunakan Transposition Cipher"""
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)


def transpose_decrypt(ciphertext, key=5):
    """Mendekripsi teks Transposition Cipher"""
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        # Jika kolom penuh, lanjut ke baris berikutnya
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# --- Contoh Uji Transposition Cipher ---
msg = "TRANSPOSITIONCIPHER"
key = 5
enc = transpose_encrypt(msg, key)
dec = transpose_decrypt(enc, key)

print("=== TRANSPOSITION CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
