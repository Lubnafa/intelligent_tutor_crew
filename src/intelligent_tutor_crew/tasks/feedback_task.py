"""Task for providing feedback to students."""

from crewai import Task
from src.agents import FeedbackAgent


def provide_feedback_task(grading_results: str, topic: str) -> Task:
    """Create and return the Provide Feedback task."""
    return Task(
        description=f"""Based on the grading results, provide comprehensive feedback:
        
        Grading Results:
        {grading_results}
        
        Topic Covered: {topic}
        
        Create a markdown-formatted feedback report that includes:
        1. Performance summary (score and overall assessment)
        2. Strengths (what the student did well)
        3. Areas for improvement (specific weak points)
        4. Recommended next steps (how to improve understanding)
        5. Encouraging closing remarks
        
        Make the feedback constructive, specific, and actionable.""",
        agent=FeedbackAgent,
        expected_output="A well-formatted markdown document with performance summary, strengths, weaknesses, and recommendations",
    )

