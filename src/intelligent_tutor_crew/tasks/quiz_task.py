"""Task for generating quiz questions."""

from crewai import Task
from src.agents import QuizAgent


def generate_quiz_task(topic_explanation: str) -> Task:
    """Create and return the Generate Quiz task."""
    return Task(
        description=f"""Based on the following topic explanation, create 3-5 quiz questions:
        
        {topic_explanation}
        
        Requirements:
        - Create multiple choice questions with 4 options each (A, B, C, D)
        - Questions should test understanding of key concepts
        - Format as JSON array with this structure:
        [{{"question": "...", "options": ["A", "B", "C", "D"], "answer": "B"}}]
        - Only output valid JSON, no additional text""",
        agent=QuizAgent,
        expected_output="A JSON array of quiz questions with questions, options, and correct answers",
    )

