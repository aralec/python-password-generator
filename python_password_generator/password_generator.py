"""
Complex password generator using Python 3.12

Script developped as a side-project, feel free rework it to fit your needs.
"""

import random
import string

from typing import Tuple


SPECIAL_CHARACTERS = "!@#$%&*_?-"


class PasswordSizeError(Exception):
    """Raised when the desired length is less than 8."""

    pass


def generate_password(desired_length: int = 12) -> str:
    """Generate a password of the desired length.

    Args:
        desired_length (int, optional): Length of the password to be generated.
        Defaults to 12.

    Returns:
        str: Generated password.

    Raises:
       TypeError: If desired length is not an integer.
       PasswordSizeError: If desired length is less than 8.
    """

    # Guard clauses :
    if not isinstance(desired_length, int):
        raise TypeError("Password length must be an integer.")
    if desired_length < 8:
        raise PasswordSizeError(
            "Password length must be at least 8 characters."
        )

    # Get the ratios of each character type :
    lr, nr, sr = _get_ratios(desired_length)
    letters = _randomize(string.ascii_lowercase, lr)
    numbers = _randomize(string.digits, nr)
    special_characters = _randomize(SPECIAL_CHARACTERS, sr)

    # Mixing upper and lowercase letters :
    # Note : could aslo have used list comprehension here
    letters = list(
        map(
            lambda letter: letter.upper()
            if random.choice((True, False))
            else letter,
            letters
        )
    )

    # Concatenation :
    password = letters + numbers + special_characters
    random.shuffle(password)

    return ''.join(password)


def _randomize(source: str, size: int) -> list[str]:
    """Get a collection of random elements from the source."""

    return [random.choice(source) for _ in range(size)]


def _get_ratios(password_length: int) -> Tuple[int, int, int]:
    """Get ratios of each character type."""

    # Half of the password length is for letters :
    letters = int(password_length / 2)

    # The other half is distributed between numbers and special characters :
    numbers_and_special_characters = password_length - letters

    if numbers_and_special_characters > int(password_length / 4):
        numbers = random.randint(1, numbers_and_special_characters // 2)
        special_characters = numbers_and_special_characters - numbers
    else:
        special_characters = numbers_and_special_characters // 2
        numbers = numbers_and_special_characters - special_characters

    return letters, numbers, special_characters


if __name__ == "__main__":
    pwd = generate_password()
    print("Generated password : ", pwd)
