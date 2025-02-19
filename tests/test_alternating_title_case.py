import pytest
from src.alternating_title_case import alternating_title_case

def test_basic_alternating_title_case():
    assert alternating_title_case("hello world") == 'Hello wOrLd'
    assert alternating_title_case("python is awesome") == 'Python iS aWeSoMe'

def test_single_word():
    assert alternating_title_case("hello") == 'Hello'
    assert alternating_title_case("world") == 'World'

def test_multiple_words():
    assert alternating_title_case("one two three four") == 'One tWo tHrEe fOuR'

def test_edge_cases():
    # Empty string
    assert alternating_title_case("") == ''
    
    # String with multiple spaces
    assert alternating_title_case("  hello   world  ") == 'Hello wOrLd'

def test_error_handling():
    # Non-string input
    with pytest.raises(TypeError):
        alternating_title_case(123)
    
    with pytest.raises(TypeError):
        alternating_title_case(None)

def test_mixed_case_input():
    assert alternating_title_case("HeLLo WoRLd") == 'Hello wOrLd'
    assert alternating_title_case("PYTHON is GREAT") == 'Python iS gReAt'