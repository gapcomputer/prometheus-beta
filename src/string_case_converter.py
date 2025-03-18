def to_alternating_path_case(input_string):
    """
    Convert a string to alternating path case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating path case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_path_case("hello world")
        'hello-WORLD'
        >>> to_alternating_path_case("python programming")
        'python-PROGRAMMING'
        >>> to_alternating_path_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Convert first word to lowercase, subsequent words to uppercase
    result = []
    for i, word in enumerate(words):
        if i == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    
    # Join with hyphen
    return '-'.join(result)