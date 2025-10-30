# XOR Cipher with Binary Key

A simple Python program that implements XOR encryption using a randomly generated binary key to encrypt and decrypt text.

## Features

- **Random binary key generation**: Creates a unique key for each message
- **XOR encryption**: Simple but effective symmetric encryption algorithm
- **Reversible process**: The same cipher is used for both encryption and decryption
- **Easy to use**: Simple command-line interface

## Requirements

- Python 3.x
- `random` module (included in Python standard library)

## Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/DGIM0106/XOR-Cipher-with-Binary-Key.git
cd XOR-Cipher-with-Binary-Key
```

2. Run the program:
```bash
python xor_cipher.py
```

3. Follow the instructions:
   - Enter the text you want to encrypt when prompted
   - The program will automatically generate a binary key
   - You will see the encrypted text and the original text verification

## Example Usage

```
Enter text to encrypt: Hello World
Generated key:  101010110110
Encrypted text: �↨��↨�▲�▼↨�
Original text: Hello World
```

## How It Works

### Key Generation
```python
def generar_clave_binaria(longitud):
    clave = ""  
    for i in range(longitud):
        clave += str(random.randint(0, 1))
    return clave
```

### XOR Encryption Algorithm
```python
def Encriptar(texto, clave):
    resultado = ""  
    for i in range(len(texto)):
        resultado += chr(ord(texto[i]) ^ int(clave[i % len(clave)]))
    return resultado
```

The XOR cipher operates bit by bit, combining each character of the text with the binary key using the exclusive OR operation.

## Limitations

- The key should be the same length as the text for maximum security
- Not suitable for production cryptographic use
- Educational purposes only

## Security Considerations

This is an educational project that demonstrates basic encryption concepts. **Should NOT be used to protect sensitive information in real environments**.
