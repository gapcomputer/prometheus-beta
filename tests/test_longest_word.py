import pytest
from src.longest_word import find_longest_word

def test_normal_sentence():
    """Test finding the longest word in a normal sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    """Test when multiple words have the same maximum length."""
    assert find_longest_word("hello world great") == "hello"

def test_sentence_with_punctuation():
    """Test sentence with punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_empty_string():
    """Test empty string input."""
    assert find_longest_word("") == ""

def test_whitespace_only():
    """Test input with only whitespace."""
    assert find_longest_word("   ") == ""

def test_single_word():
    """Test with a single word."""
    assert find_longest_word("python") == "python"

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(["hello", "world"])