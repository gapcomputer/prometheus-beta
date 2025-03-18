def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The input string converted to CONSTANT_CASE.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("camelCaseString")
        'CAMEL_CASE_STRING'
        >>> to_constant_case("snake_case_string")
        'SNAKE_CASE_STRING'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert different case formats to constant case
    # First, handle existing separators
    result = input_string.replace('-', ' ').replace('_', ' ')
    
    # Split by camel case (insert space before capital letters)
    chars = []
    for i, char in enumerate(result):
        # Add space before uppercase letters, with special handling for consecutive uppercase
        if (i > 0 and 
            char.isupper() and 
            (result[i-1].islower() or  # Lowercase to uppercase transition
             (i > 1 and result[i-1].isupper() and result[i-2].islower()))):  # Special case for mixedCAMELCase
            chars.append(' ')
        chars.append(char)
    
    # Join and convert to upper case, replace spaces with underscores
    result = ''.join(chars).upper().replace(' ', '_')
    
    return result