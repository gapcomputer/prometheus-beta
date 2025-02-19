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
            # Odd index words (1, 3, 5...) alternate case manually
            lower_word = word.lower()
            chars = [
                lower_word[j].upper() if j % 2 == 1 else lower_word[j]
                for j in range(len(lower_word))
            ]
            alternating_words.append(''.join(chars))
    
    return ' '.join(alternating_words)