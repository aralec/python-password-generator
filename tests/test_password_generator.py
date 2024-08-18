"""
Unit tests for the complex password generator.
"""

import pytest

from python_password_generator import generate_password, PasswordSizeError


def test_generate_password_length():
    # Test generate_password with a length of 12 (default)
    password = generate_password()
    assert len(password) == 12


@pytest.mark.parametrize("length", [8, 16, 32])
def test_generate_password_lengths(length):
    password = generate_password(desired_length=length)
    assert len(password) == length


def test_generate_password_min_length():
    with pytest.raises(PasswordSizeError):
        generate_password(desired_length=6)


def test_generate_password_type_mixture():
    # Test that the password contains a mix of characters
    password = generate_password()
    assert any(c.isalpha() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%&*_?-" for c in password)
