def to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case (alternating uppercase and lowercase).
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'HeLlO'
        >>> to_sponge_case("WORLD")
        'WoRlD'
        >>> to_sponge_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Convert to sponge case
    return ''.join(c.upper() if i % 2 == 0 else c.lower() 
                   for i, c in enumerate(text))