from cryptography.fernet import Fernet
import os

# Retrieve the key from an environment variable
secret_key = 'jq6D8X4vuJHhDlyr2NB-COFOUFaH88VNgnFq5iM3WZc='
if not secret_key:
    raise ValueError("No secret encryption key found")

cipher_suite = Fernet(secret_key)

def encrypt_message(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message
