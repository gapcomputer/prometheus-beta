from datetime import datetime

def get_current_time_formatted() -> str:
    """
    Returns the current time in HH:MM:SS format.

    Returns:
        str: Current time formatted as 'HH:MM:SS' (24-hour format)
    
    Examples:
        >>> get_current_time_formatted()  # might return '14:30:45'
    """
    return datetime.now().strftime('%H:%M:%S')