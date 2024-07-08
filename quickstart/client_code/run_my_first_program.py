from nada_dsl import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, y, x = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        y, x = x - q * y, y
    return x + m0 if x < 0 else x

def rsa_encrypt(message, n, e):
    return message**e % n

def rsa_decrypt(ciphertext, n, d):
    return ciphertext**d % n

def nada_main():
    party1 = Party(name="Party1")
    p = SecretInteger(Input(name="p", party=party1))
    q = SecretInteger(Input(name="q", party=party1))
    message = SecretInteger(Input(name="message", party=party1))

    # Step 1: Calculate n
    n = p * q

    # Step 2: Calculate Euler's Totient function φ(n)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 3
    while gcd(e, phi_n) != 1:
        e += 2

    # Step 4: Calculate d such that d * e ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi_n)

    # Encrypt the message
    encrypted_message = rsa_encrypt(message, n, e)

    # Decrypt the message
    decrypted_message = rsa_decrypt(encrypted_message, n, d)

    # Return the encrypted and decrypted message as outputs
    return [
        Output(encrypted_message, "encrypted_message", party1),
        Output(decrypted_message, "decrypted_message", party1)
    ]

# Example input and expected output
if __name__ == "__main__":
    p = 61
    q = 53
    message = 65

    # Example output using non-secret values
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi_n) != 1:
        e += 2
    d = mod_inverse(e, phi_n)

    # Encrypt and decrypt the message
    encrypted_message = rsa_encrypt(message, n, e)
    decrypted_message = rsa_decrypt(encrypted_message, n, d)

    print("Public Key (n, e):", (n, e))
    print("Private Key (n, d):", (n, d))
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)
