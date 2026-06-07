# main.py
from encryption import encrypt
from decryption import decrypt

# Sender side
message = input("Enter message: ")
encrypted, session_key = encrypt(message)
print(f"Encrypted: {encrypted}")

# Receiver side
decrypted = decrypt(encrypted, session_key)
print(f"Decrypted: {decrypted}")