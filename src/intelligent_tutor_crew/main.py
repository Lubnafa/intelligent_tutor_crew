"""Main entry point for the Intelligent Tutor Crew application."""

import os
from dotenv import load_dotenv
from .crew import create_intelligent_tutor_crew

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
    topic = "Python list comprehensions"
    print(f"📚 Topic: {topic}\n")
    
    # Create and run crew
    crew = create_intelligent_tutor_crew(topic=topic)
    result = crew.kickoff()
    
    print("\n✅ Crew run complete!\n")
    print("=" * 80)
    print("RESULT:")
    print("=" * 80)
    print(result)
    
    return result


if __name__ == "__main__":
    main()

