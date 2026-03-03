# ============================================================
# IMPLEMENTASI ALGORITMA RSA DARI SCRATCH
# Tanpa menggunakan library enkripsi instan
# ============================================================

import random

# ============================================================
# 1. FUNGSI MATEMATIKA DASAR
# ============================================================

def gcd(a, b):
    """Menghitung Greatest Common Divisor (FPB)"""
    while b != 0:
        a, b = b, a % b
    return a


def extended_euclidean(a, b):
    """
    Extended Euclidean Algorithm
    Digunakan untuk mencari invers modular
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd_value, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_value, x, y


def mod_inverse(e, phi):
    """
    Mencari d sehingga:
    d * e ≡ 1 (mod phi)
    """
    gcd_value, x, y = extended_euclidean(e, phi)

    if gcd_value != 1:
        raise Exception("Invers modular tidak ada!")
    else:
        return x % phi


def modular_exponentiation(base, exponent, modulus):
    """
    Menghitung (base^exponent) mod modulus
    menggunakan metode efisien (square and multiply)
    """
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent // 2
        base = (base * base) % modulus

    return result


# ============================================================
# 2. KEY GENERATION
# ============================================================

def generate_keys():
    print("\n=== PEMBANGKITAN KUNCI (KEY GENERATION) ===")

    # Gunakan prima kecil
    p = 61
    q = 53

    print(f"Bilangan prima p = {p}")
    print(f"Bilangan prima q = {q}")

    # Hitung n
    n = p * q
    print(f"Modulus n = p × q = {n}")

    # Hitung totient Euler
    phi = (p - 1) * (q - 1)
    print(f"φ(n) = (p-1)(q-1) = {phi}")

    # Pilih e
    e = 17
    print(f"Nilai e yang dipilih = {e}")

    # Hitung d
    d = mod_inverse(e, phi)
    print(f"Nilai d (invers modular dari e) = {d}")

    print("\nPublic Key  = (e, n) =", (e, n))
    print("Private Key = (d, n) =", (d, n))

    return (e, n), (d, n)


# ============================================================
# 3. ENKRIPSI
# ============================================================

def encrypt(public_key, plaintext):
    print("\n=== PROSES ENKRIPSI ===")
    e, n = public_key

    ciphertext = []

    for char in plaintext:
        m = ord(char)  # ubah huruf ke ASCII
        c = modular_exponentiation(m, e, n)
        ciphertext.append(c)

        print(f"Plaintext '{char}' -> ASCII {m} -> Cipher {c}")

    return ciphertext


# ============================================================
# 4. DEKRIPSI
# ============================================================

def decrypt(private_key, ciphertext):
    print("\n=== PROSES DEKRIPSI ===")
    d, n = private_key

    plaintext = ""

    for c in ciphertext:
        m = modular_exponentiation(c, d, n)
        char = chr(m)
        plaintext += char

        print(f"Cipher {c} -> ASCII {m} -> Plaintext '{char}'")

    return plaintext


# ============================================================
# 5. PROGRAM UTAMA
# ============================================================

def main():
    print("================================================")
    print("IMPLEMENTASI ALGORITMA RSA")
    print("Rivest, Shamir, dan Adleman (1977)")
    print("================================================")

    # Generate Key
    public_key, private_key = generate_keys()

    # Input pesan
    message = input("\nMasukkan pesan yang ingin dienkripsi: ")

    # Enkripsi
    cipher = encrypt(public_key, message)
    print("\nCiphertext:", cipher)

    # Dekripsi
    decrypted_message = decrypt(private_key, cipher)
    print("\nHasil Dekripsi:", decrypted_message)


if __name__ == "__main__":
    main()
