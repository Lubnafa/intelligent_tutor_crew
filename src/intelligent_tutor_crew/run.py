"""Wrapper script for crewai run command."""

import os
import sys
from pathlib import Path

# Add project root to Python path so we can import main
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Now import and run main
import main

def run():
    """Entry point for crewai run command."""
    main.main()

if __name__ == "__main__":
    run()
