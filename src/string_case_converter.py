import re

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
    
    # Replace existing separators with spaces
    result = input_string.replace('-', ' ').replace('_', ' ')
    
    # Use regex to split camel case
    # This handles various cases like camelCase, PascalCase, mixedCAMELCase
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', result)
    
    # Convert to uppercase and replace spaces with underscores
    result = result.upper().replace(' ', '_')
    
    return result