import pytest
from src.string_case_converter import to_constant_case

def test_basic_string_conversion():
    """Test basic string to constant case conversion."""
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("helloWorld") == "HELLO_WORLD"
    assert to_constant_case("hello-world") == "HELLO_WORLD"
    assert to_constant_case("hello_world") == "HELLO_WORLD"

def test_camel_case_conversion():
    """Test conversion of camel case strings."""
    assert to_constant_case("camelCaseString") == "CAMEL_CASE_STRING"
    assert to_constant_case("mixedCAMELCase") == "MIXED_CAMEL_CASE"

def test_existing_snake_case():
    """Test conversion of existing snake case strings."""
    assert to_constant_case("existing_snake_case") == "EXISTING_SNAKE_CASE"

def test_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_constant_case("mixed-snake_caseString") == "MIXED_SNAKE_CASE_STRING"

def test_empty_string():
    """Test conversion of empty string."""
    assert to_constant_case("") == ""
    assert to_constant_case("  ") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_constant_case("hello") == "HELLO"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_constant_case(None)
    
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(["list"])