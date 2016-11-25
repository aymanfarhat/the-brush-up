def unique_characters (input_str):
    """Implement an algorithm to determine if a string has all unique characters."""
    char_hash = set()

    for c in input_str:
        if c in char_hash:
            print(c)
            return False
        else:
            char_hash.add(c)

    return True
