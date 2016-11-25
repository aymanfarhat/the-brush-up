def compress_string(text):
    """
    Implement a method to perform basic string compression
    using the counts of repeated characters. For example,
    the string aabcccccaaa would become a2blc5a3.
    If the "compressed" string would not become smaller
    than the orig- inal string, your method should return the original string.
    """
    compressed_str = []
    current_count = 1

    for i in range(len(text)):
        current_char = text[i]

        if i < len(text) - 1 and text[i + 1] == text[i]:
            current_count += 1
        else:
            compressed_str.append(current_char + str(current_count))

            current_count = 1

    result = ''.join(compressed_str)

    return result if len(result) < len(text) else text
