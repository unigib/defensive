def parse_count(text):
    try:
        count = int(text.strip())
    except ValueError:
        raise ValueError("Enter a whole number.")

    if not 1 <= count <= 10:
        raise ValueError("Use a number from 1 to 10.")

    return count
