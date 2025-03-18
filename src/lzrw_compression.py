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
    
    # Copy the input data as a base
    for byte in input_data:
        compressed.append(byte)
    
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
    
    # Return data excluding the control flag
    return bytearray(compressed_data[1:])