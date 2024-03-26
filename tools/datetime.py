from crewai_tools import tool

@tool("Check time")
def get_time(timezone: str) -> str:
    """Returns current time in timezone."""
    # get current time
    
    # Function logic here