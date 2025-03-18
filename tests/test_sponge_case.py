import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic sponge case conversion."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_already_uppercase_string():
    """Test converting an uppercase string."""
    assert to_sponge_case("HELLO") == "HeLlO"

def test_already_lowercase_string():
    """Test converting a lowercase string."""
    assert to_sponge_case("world") == "WoRlD"

def test_mixed_case_string():
    """Test converting a mixed case string."""
    assert to_sponge_case("HeLLo") == "HeLlO"

def test_empty_string():
    """Test converting an empty string."""
    assert to_sponge_case("") == ""

def test_string_with_numbers():
    """Test converting a string with numbers."""
    assert to_sponge_case("hello123") == "HeLlO123"

def test_string_with_special_characters():
    """Test converting a string with special characters."""
    assert to_sponge_case("hello!world") == "HeLlO!WoRlD"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(["hello"])