import lzma
import io

def lzma_compress(data: str, compression_level: int = 6) -> bytes:
    """
    Compress a given string using LZMA compression.

    Args:
        data (str): The input string to compress.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default in LZMA).

    Returns:
        bytes: Compressed data.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert string to bytes and compress
    try:
        compressed_data = lzma.compress(
            data.encode('utf-8'), 
            preset=compression_level
        )
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzma_decompress(compressed_data: bytes) -> str:
    """
    Decompress LZMA compressed data back to a string.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        str: Decompressed string.

    Raises:
        TypeError: If input is not bytes.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress
    try:
        decompressed_data = lzma.decompress(compressed_data)
        return decompressed_data.decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")