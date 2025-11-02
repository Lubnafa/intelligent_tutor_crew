"""Main entry point for the Intelligent Tutor Crew application."""

import os
from dotenv import load_dotenv
from .crew import IntelligentTutorCrew

# Load environment variables
load_dotenv()

# Verify API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError(
        "GOOGLE_API_KEY not found in environment variables. "
        "Please set it in your .env file."
    )


def main():
    """Run the Intelligent Tutor Crew."""
    print("🚀 Starting Intelligent Tutor Crew...\n")
    
    # Example usage - you can modify this to accept user input
    inputs = {
        'topic': 'Python list comprehensions',
        'student_answers': ''
    }
    
    # Create and run crew
    crew = IntelligentTutorCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    print("\n✅ Crew run complete!\n")
    print("=" * 80)
    print("RESULT:")
    print("=" * 80)
    print(result)
    
    return result


if __name__ == "__main__":
    main()


