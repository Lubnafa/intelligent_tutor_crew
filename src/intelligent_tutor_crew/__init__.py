"""Intelligent Tutor Crew - Main package."""

from .crew import IntelligentTutorCrew

# Export main function for entry point
def main():
    """Main entry point for crewai run command."""
    from .main import main as _main
    return _main()

__all__ = ["IntelligentTutorCrew", "main"]
__version__ = "0.1.0"

