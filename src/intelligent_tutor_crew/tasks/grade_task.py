"""Task for grading student answers."""

from crewai import Task
from src.agents import GraderAgent


def grade_answers_task(quiz_questions: str, student_answers: str) -> Task:
    """Create and return the Grade Answers task."""
    return Task(
        description=f"""Grade the following student answers against the quiz questions:
        
        Quiz Questions:
        {quiz_questions}
        
        Student Answers:
        {student_answers}
        
        For each question:
        1. Compare the student's answer with the correct answer
        2. Mark as correct or incorrect
        3. If incorrect, provide a brief explanation
        4. Calculate an overall score out of 100
        
        Format your response as JSON:
        {{
            "score": 85,
            "total_questions": 5,
            "correct": 4,
            "incorrect": 1,
            "results": [
                {{"question": 1, "correct": true, "explanation": ""}},
                {{"question": 2, "correct": false, "explanation": "..."}}
            ]
        }}""",
        agent=GraderAgent,
        expected_output="A JSON object with score, results, and explanations for each question",
    )

