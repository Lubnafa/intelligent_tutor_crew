"""Task for teaching a topic."""

from crewai import Task
from src.agents import TeacherAgent


def teach_topic_task(topic: str) -> Task:
    """Create and return the Teach Topic task."""
    return Task(
        description=f"""Explain the topic: {topic}
        
        Provide a comprehensive explanation that includes:
        1. A clear definition and overview
        2. Step-by-step breakdown of key concepts
        3. Practical examples
        4. Three key takeaways the student should remember
        
        Format your response in clear, educational markdown.""",
        agent=TeacherAgent,
        expected_output="A well-structured markdown explanation with examples and three key takeaways",
    )

