def is_permutation (str_1, str_2):
    """
    Given two strings, write a method to 
    decide if one is a permutation of the other.
    """
    character_ref = {}

    if len(str_1) != len(str_2):
        return False
        
    for c in str_1:
        if c not in character_ref:
            character_ref[c] = 1
        else:
            character_ref[c] += 1

    for c in str_2:
        if c in character_ref:
            character_ref[c] -= 1
        else:
            return False

    return not all(character_ref.values())
