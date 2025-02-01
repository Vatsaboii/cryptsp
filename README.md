# Cryptsp: Next Generation Unified Cryptography Library

## Secure, Powerful, and Ready for the Future
Welcome to Cryptsp, a modern cryptography library designed to simplify and enhance your encryption, decryption, and security workflows. Whether you're a beginner or a seasoned developer, Cryptsp is your go-to toolkit for building robust, secure applications.

## Introduction

**Cryptsp** is a powerful and easy-to-use cryptography library that combines multiple cryptographic techniques under a single package. It supports:
- **Symmetric Encryption**: AES, ChaCha20, Salsa20
- **Asymmetric Encryption**: RSA, ECC
- **Key Derivation**: PBKDF2, Argon2
- **Hashing & Digital Signatures**: SHA-256, HMAC, RSA Signatures

This library simplifies cryptographic operations by integrating multiple libraries into a unified interface, allowing users to encrypt, decrypt, sign, and verify data with minimal effort.

## Benefits of Using Cryptsp

- **Unparalleled Security**: Built on industry-leading cryptography libraries like PyCryptodome and JWT, Cryptsp ensures your data is encrypted with state-of-the-art algorithms.
- **Lightweight and Fast**: Designed to perform without draining resources, Cryptsp is highly efficient even on systems with limited capacity.
- **Ease of Use**: Simple function calls to encrypt, decrypt, and sign data.
- **Versatility**: Supports both symmetric and asymmetric encryption along with key derivation and hashing.
- **Security**: Encrypt and decrypt files with support for multiple algorithms, making it a perfect fit for securing sensitive data in transit or storage.
- **Developer-Friendly**: Easy-to-use functions save time and reduce the complexity of writing cryptographic code.

## Installation 🛠️

To install **Cryptsp**, use the following command:

```bash
pip install cryptsp
```

## Example Usage
### 1. Encrypt and Decrypt with AES

```python
from cryptsp import AES

key = AES.generate_key()
plaintext = "Hello, Cryptsp!"
ciphertext, nonce = AES.encrypt(plaintext, key)
decrypted_text = AES.decrypt(ciphertext, key, nonce)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
```

### 2. RSA Encryption and Decryption

```python
from cryptsp import RSA

public_key, private_key = RSA.generate_keys()
message = "Secure Message"
ciphertext = RSA.encrypt(message, public_key)
decrypted_message = RSA.decrypt(ciphertext, private_key)

print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
```

## GitHub Repository
For more examples and documentation, visit the official repository:
[GitHub - Cryptsp](https://github.com/Vatsaboii/cryptsp)

## Extensibility 🔧
Open-source and modular, so you can easily add new encryption algorithms or customize it for your use case.

## Conclusion

Cryptsp makes cryptographic operations straightforward by wrapping multiple libraries into a single package. Whether you're encrypting sensitive data, signing messages, or generating secure keys, **Cryptsp** provides a seamless experience.

---

Give it a try and enhance the security of your applications with **Cryptsp**!
