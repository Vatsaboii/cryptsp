import sys
import os
from base64 import b64encode #necessary to import this library for Argon2 and PBKDF2

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cryptsp
from cryptsp import CryptoManager


# Example usage of all methods
manager = CryptoManager()
key = manager.generate_key()

# AES-GCM
encrypted_data = manager.encrypt_aes("Hello, AES-GCM!", key, mode='GCM')
decrypted_data = manager.decrypt_aes(encrypted_data, key)
print("Decrypted (AES-GCM):", decrypted_data.decode())

# AES-CBC
encrypted_data = manager.encrypt_aes("Hello, AES-CBC!", key, mode='CBC')
decrypted_data = manager.decrypt_aes(encrypted_data, key)
print("Decrypted (AES-CBC):", decrypted_data.decode())

# AES-CTR
encrypted_data = manager.encrypt_aes("Hello, AES-CTR!", key, mode='CTR')
decrypted_data = manager.decrypt_aes(encrypted_data, key)
print(decrypted_data.decode())  # Output: Hello, AES-CTR!

# ChaCha20
encrypted_data = manager.encrypt_chacha20("Hello, ChaCha20!", key)
decrypted_data = manager.decrypt_chacha20(encrypted_data, key)
print("Decrypted (ChaCha20):", decrypted_data.decode())

# Salsa20
encrypted_data = manager.encrypt_salsa20("Hello, Salsa20!", key)
decrypted_data = manager.decrypt_salsa20(encrypted_data, key)
print(decrypted_data.decode())  # Output: Hello, Salsa20!

# ECIES
private_key, public_key = manager.generate_ecc_keypair()
encrypted_data = manager.encrypt_ecies("Hello, ECIES!", public_key)
decrypted_data = manager.decrypt_ecies(encrypted_data, private_key)
print(decrypted_data.decode())  # Output: Hello, ECIES!

#Argon2
key, salt = manager.derive_key("my_password", algorithm='Argon2')
print(f"Derived key: {b64encode(key).decode()}")

data_to_encrypt = "Hello, Argon2!"
encrypted_data = manager.encrypt_aes(data_to_encrypt, key, mode='GCM')
decrypted_data = manager.decrypt_aes(encrypted_data, key)
print("Decrypted Data:", decrypted_data.decode())

# RSA
private_key, public_key = manager.generate_rsa_keypair()
encrypted_data = manager.encrypt_rsa("Hello, RSA!", public_key)
decrypted_data = manager.decrypt_rsa(encrypted_data, private_key)
print("Decrypted (RSA):", decrypted_data.decode())

# # PBKDF2
key, salt = manager.derive_key("my_password", algorithm='PBKDF2')
print(f"Derived key (PBKDF2): {b64encode(key).decode()}")

# HMAC
data = "Hello, HMAC!"
hmac = manager.create_hmac(data, key, hash_algo='SHA256')
is_valid = manager.verify_hmac(data, hmac, key, hash_algo='SHA256')
print("HMAC Valid:", is_valid)

# Digital Signatures (RSA)
data = "Hello, Signature!"
signature = manager.sign_data(data, private_key)
is_valid = manager.verify_signature(data, signature, public_key)
print("Signature Valid (RSA):", is_valid)

# Digital Signatures (ECC)
data = "Hello, ECC Signature!"
signature = manager.sign_data(data, private_key)
is_valid = manager.verify_signature(data, signature, public_key)
print("Signature Valid (ECC):", is_valid)


file_path = "/Users/srivatsapalepu/cryptsp/example.txt"
encrypted_file = manager.encrypt_file(file_path, key, algorithm='AES-GCM')
decrypted_file = manager.decrypt_file(encrypted_file, key)

with open(decrypted_file, "r") as f:
    print("Decrypted File Content:", f.read())
