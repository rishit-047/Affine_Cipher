# Affine-Cipher-Encryption-Decryption-Tool
A Python-based tool that implements the classic **Affine Cipher** for both encryption and decryption over all printable ASCII characters (ASCII codes 32–126).  
Supports case-sensitive encryption, numbers, special characters, and can process text provided via command-line or from a file.  

Designed for educational use, secure local message encryption, and cryptography experimentation.

## Features
- **Complete Printable ASCII Support**: Encrypts and decrypts all characters from ASCII 32 to 126, including letters, digits, symbols, and whitespace.
- **Customizable Keys**: Supports user-defined keys `a` and `b` (with validation to ensure `a` and modulus=95 are coprime).
- **Case Sensitive**: Maintains the original case of letters and preserves numbers and special characters.
- **Separate Encryption & Decryption Scripts**: Includes two dedicated scripts: `encrypt.py` for encryption and `decrypt.py` for decryption.
- **Flexible Input Options**: Accepts plaintext or ciphertext directly from the command line or by reading from a text file.
- **Clean Python Implementation**: Uses modular arithmetic to ensure all results map to printable ASCII characters.
- **Command-Line Tool**: Simple CLI interface for quick testing and usage.

## Requirements
- **Python 3.6+** – Required to run the scripts.
- **Python Standard Libraries Only**:
  - `math` – To calculate the modular inverse.
  - `sys` – To handle command-line arguments.

No external dependencies are needed.

## How It Works
- **Modulus**: 95 (covers ASCII 32–126 inclusive).
- **Encryption**: E(x) = (a * x + b) % 95
- **Decryption**: D(y) = a_inv * (y - b) % 95
  where `a_inv` is the modular inverse of `a` modulo 95.

All characters are mapped to their ASCII codes, normalized by subtracting 32, processed, then mapped back by adding 32.

## Files
- `encrypt.py` – Python script to encrypt text.
- `decrypt.py` – Python script to decrypt text.
- `README.md` – Project documentation (this file).






