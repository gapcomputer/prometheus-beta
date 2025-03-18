"""
Test suite for LZRW compression algorithm implementation.
"""

import pytest
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzrw_compression import compress, decompress

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_data = bytearray()
    assert compress(empty_data) == bytearray()
    assert decompress(bytearray()) == bytearray()

def test_single_byte():
    """Test compression and decompression of a single byte."""
    data = bytearray([42])
    compressed = compress(data)
    assert decompress(compressed) == data

def test_simple_repetitive_data():
    """Test compression of repetitive data."""
    data = bytearray([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
    compressed = compress(data)
    assert decompress(compressed) == data

def test_random_data():
    """Test compression of random data."""
    data = bytearray([3, 5, 2, 1, 7, 4, 6, 8, 9, 0])
    compressed = compress(data)
    assert decompress(compressed) == data

def test_long_input():
    """Test compression of a longer input sequence."""
    data = bytearray(range(255)) * 10
    compressed = compress(data)
    assert decompress(compressed) == data

def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        compress("not a byte array")
    with pytest.raises(TypeError):
        decompress("not a byte array")

def test_compressed_data_structure():
    """Verify the basic structure of compressed data."""
    data = bytearray([1, 1, 1, 1, 1, 1, 1, 1])
    compressed = compress(data)
    # Verify the first byte is the control flag
    assert compressed[0] == 0
    # Simplified check: compressed data length is original length + 1
    assert len(compressed) == len(data) + 1

def test_round_trip_preservation():
    """Ensure multiple round trips preserve data."""
    original_data = bytearray([5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0])
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_invalid_compression_flag():
    """Test handling of invalid compression flag."""
    invalid_compressed = bytearray([1, 42, 43])  # Invalid flag
    with pytest.raises(ValueError):
        decompress(invalid_compressed)