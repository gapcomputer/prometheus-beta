"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides a basic implementation of the LZRW compression algorithm.
LZRW is a fast compression algorithm that trades some compression ratio 
for speed.
"""

def compress(input_data):
    """
    Compress input data using the LZRW compression algorithm.
    
    Args:
        input_data (bytes or bytearray): The data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
    """
    # Validate input
    if not isinstance(input_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    # If input is empty, return empty bytearray
    if not input_data:
        return bytearray()
    
    # Initialize compression structures
    compressed = bytearray()
    window_size = 4096
    
    # Add control flag for tracking compression type
    compressed.append(0)  # 0 indicates compression used
    
    # Sliding window compression
    start = 0
    while start < len(input_data):
        # Look for longest match
        longest_match_length = 0
        longest_match_offset = 0
        
        # Search backwards in the sliding window
        window_start = max(0, start - window_size)
        for match_start in range(window_start, start):
            match_length = 0
            while (start + match_length < len(input_data) and 
                   match_length < 15 and  # Limit match length 
                   input_data[match_start + match_length] == input_data[start + match_length]):
                match_length += 1
            
            if match_length > longest_match_length:
                longest_match_length = match_length
                longest_match_offset = start - match_start
        
        # Encode match or literal
        if longest_match_length > 2:
            # Encode match: 4 bits for offset, 4 bits for length
            match_token = ((longest_match_offset & 0xF) << 4) | (longest_match_length & 0xF)
            compressed.append(match_token)
            start += longest_match_length
        else:
            # Encode literal
            compressed.append(input_data[start])
            start += 1
    
    return compressed

def decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes or bytearray): The data to be decompressed
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If compressed data is invalid
    """
    # Validate input
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    # Check for empty input
    if not compressed_data:
        return bytearray()
    
    # Check compression flag
    if compressed_data[0] != 0:
        raise ValueError("Invalid compression format")
    
    # Initialize decompression
    decompressed = bytearray()
    pos = 1  # Start after control flag
    
    while pos < len(compressed_data):
        # Get the token
        token = compressed_data[pos]
        pos += 1
        
        # Check if it's a match or literal
        if token >= 16:
            # Literal byte
            decompressed.append(token)
        else:
            # Match token: 4 bits offset, 4 bits length
            match_offset = token >> 4
            match_length = token & 0xF
            
            # If zero match_offset, it's an invalid token
            if match_offset == 0:
                break
            
            # Find match start in decompressed data
            match_start = len(decompressed) - match_offset
            
            # Prevent index out of range
            if match_start < 0:
                break
            
            # Copy matched sequence
            for _ in range(match_length):
                if match_start >= len(decompressed):
                    break
                byte_to_copy = decompressed[match_start]
                decompressed.append(byte_to_copy)
                match_start += 1
    
    return decompressed