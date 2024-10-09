import random
import string

def generate_pattern(pattern):
    """Generates a new pattern based on the given pattern.

    Args:
        pattern: The original pattern to be modified.

    Returns:
        A new pattern with modified letters and numbers.
    """

    new_pattern = ""
    for char in pattern:
        if char.isalpha():
            new_char = random.choice(string.ascii_uppercase)
        elif char.isdigit():
            new_char = random.choice(string.digits)
        else:
            new_char = char
        new_pattern += new_char
    return new_pattern

def main():
    """Generates and prints 1000 similar patterns based on the given pattern."""

    pattern = "MTMD-666R-GQB6"
    for _ in range(1000):
        print(generate_pattern(pattern))

if __name__ == "__main__":
    main()

