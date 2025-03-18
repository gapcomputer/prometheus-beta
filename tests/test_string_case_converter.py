import pytest
from src.string_case_converter import to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_path_case("hello world") == "hello-WORLD"
    assert to_alternating_path_case("python programming") == "python-PROGRAMMING"

def test_single_word():
    """Test conversion with a single word"""
    assert to_alternating_path_case("hello") == "hello"

def test_empty_string():
    """Test conversion of empty string"""
    assert to_alternating_path_case("") == ""

def test_multiple_words():
    """Test conversion with multiple words"""
    assert to_alternating_path_case("a b c d") == "a-B-C-D"

def test_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(None)

def test_whitespace_handling():
    """Test handling of multiple whitespaces"""
    assert to_alternating_path_case("  hello   world  ") == "hello-WORLD"

def test_mixed_case_input():
    """Test input with mixed case"""
    assert to_alternating_path_case("Hello WORLD Python") == "hello-WORLD-PYTHON"