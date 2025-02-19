def alternating_title_case(input_string):
    """
    Convert a string to alternating title case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with alternating case for each word.
    
    Examples:
        >>> alternating_title_case("hello world")
        'Hello wOrLd'
        >>> alternating_title_case("python is awesome")
        'Python iS aWeSoMe'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    words = input_string.split()
    alternating_words = []
    
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) are title case
            alternating_words.append(word.title())
        else:
            # Odd index words (1, 3, 5...) have alternating character case
            chars = list(word.lower())
            for j in range(1, len(chars), 2):
                chars[j] = chars[j].upper()
            alternating_words.append(''.join(chars))
    
    result = ' '.join(alternating_words)
    return result