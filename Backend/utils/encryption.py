from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

encryption_key = os.getenv("FERNET_KEY")
cipher = Fernet(encryption_key)

def encrypt_file_content(content: bytes) -> bytes:
    return cipher.encrypt(content)
