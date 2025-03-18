import pytest
import sys
import os
import random

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzma_compression import lzma_compress, lzma_decompress

def test_lzma_compression_and_decompression():
    """Test basic compression and decompression"""
    original_text = "Hello, this is a test of LZMA compression!"
    compressed = lzma_compress(original_text)
    assert compressed != original_text.encode('utf-8')
    
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_text

def test_different_compression_levels():
    """Test different compression levels with a more complex input"""
    # Generate a larger, more random string to test compression level differences
    def generate_random_text(length):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ') for _ in range(length))
    
    original_text = generate_random_text(1000)
    
    # Compress with low and high compression levels
    compressed_low = lzma_compress(original_text, compression_level=1)
    compressed_high = lzma_compress(original_text, compression_level=9)
    
    # Verify that compressed sizes are different
    assert len(compressed_low) != len(compressed_high)
    
    # Ensure both can be decompressed correctly
    assert lzma_decompress(compressed_low) == original_text
    assert lzma_decompress(compressed_high) == original_text

def test_invalid_compression_level():
    """Test invalid compression level raises ValueError"""
    with pytest.raises(ValueError):
        lzma_compress("Test", compression_level=10)
    
    with pytest.raises(ValueError):
        lzma_compress("Test", compression_level=-1)

def test_invalid_input_types():
    """Test input type validation"""
    # Test non-string input for compression
    with pytest.raises(TypeError):
        lzma_compress(12345)
    
    # Test non-bytes input for decompression
    with pytest.raises(TypeError):
        lzma_decompress("Not bytes")

def test_empty_string():
    """Test compression and decompression of empty string"""
    original_text = ""
    compressed = lzma_compress(original_text)
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_text

def test_non_ascii_text():
    """Test compression of non-ASCII text"""
    original_text = "こんにちは世界！ Hello World! 🌍"
    compressed = lzma_compress(original_text)
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_text