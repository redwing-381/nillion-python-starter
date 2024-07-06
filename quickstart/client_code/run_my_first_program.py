from nada_dsl import *
import math

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def mod_inverse(a, m):
    m0, y, x = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def rsa_encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)

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

    # Public and private keys
    public_key = (n, e)
    private_key = (n, d)

    # Encrypt the message
    encrypted_message = rsa_encrypt(message, public_key)

    # Decrypt the message
    decrypted_message = rsa_decrypt(encrypted_message, private_key)

    # Return the encrypted and decrypted message as outputs
    return [
        Output(encrypted_message, "encrypted_message", party1),
        Output(decrypted_message, "decrypted_message", party1)
    ]