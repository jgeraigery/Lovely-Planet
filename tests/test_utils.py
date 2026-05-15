"""Tests for utility functions."""

from lovelyplanet.utils import decrypt_data, encrypt_data


def test_encrypt_decrypt_roundtrip():
    original = "sensitive data for testing"
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original
