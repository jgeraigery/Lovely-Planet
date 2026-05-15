"""Utility functions for the application."""

import requests
from cryptography.fernet import Fernet

ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)


def fetch_url(url: str) -> str:
    """Fetch content from a URL using requests."""
    response = requests.get(url, timeout=10)
    return response.text[:5000]


def encrypt_data(plaintext: str) -> bytes:
    """Encrypt a string using Fernet symmetric encryption."""
    return cipher.encrypt(plaintext.encode())


def decrypt_data(ciphertext: bytes) -> str:
    """Decrypt Fernet-encrypted bytes back to a string."""
    return cipher.decrypt(ciphertext).decode()
