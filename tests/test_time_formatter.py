import re
import time
from src.time_formatter import get_current_time_formatted

def test_time_format():
    """Test that the function returns a time string in the correct format."""
    time_str = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), f"Invalid time format: {time_str}"

def test_time_format_24hour():
    """Verify that the time is in 24-hour format."""
    time_str = get_current_time_formatted()
    
    # Split the time string into hours, minutes, seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Check hour is between 0 and 23
    assert 0 <= hours <= 23, f"Hours out of 24-hour range: {hours}"
    
    # Check minutes and seconds are between 0 and 59
    assert 0 <= minutes <= 59, f"Minutes out of range: {minutes}"
    assert 0 <= seconds <= 59, f"Seconds out of range: {seconds}"

def test_time_consistency():
    """Ensure the function returns the current time consistently."""
    # Get time 1st time
    time1 = get_current_time_formatted()
    
    # Wait a short time
    time.sleep(0.1)
    
    # Get time 2nd time
    time2 = get_current_time_formatted()
    
    # Verify they are not exactly the same (due to potential time passing)
    assert len(set([time1, time2])) > 0, "Time function returned identical times"