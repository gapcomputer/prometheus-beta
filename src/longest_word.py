def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): The input sentence to search for the longest word.
    
    Returns:
        str: The longest word in the sentence. 
             If multiple words have the same maximum length, returns the first occurrence.
             If the sentence is empty, returns an empty string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # If sentence is empty or contains only whitespace, return empty string
    if not sentence.strip():
        return ""
    
    # Split the sentence into words, removing common punctuation
    words = sentence.replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    # If no words after splitting, return empty string
    if not words:
        return ""
    
    # Return the longest word (first occurrence if multiple words have same length)
    return max(words, key=len)