"""Basic tests for the Intelligent Tutor Crew."""

import pytest
from src.intelligent_tutor_crew.crew import create_intelligent_tutor_crew


def test_crew_creation():
    """Test that crew can be created."""
    crew = create_intelligent_tutor_crew(topic="test topic")
    assert crew is not None
    assert len(crew.agents) > 0
    assert len(crew.tasks) > 0


def test_crew_with_answers():
    """Test crew creation with student answers."""
    crew = create_intelligent_tutor_crew(
        topic="test topic",
        student_answers="test answers"
    )
    assert crew is not None
    assert len(crew.tasks) >= 2  # Should have at least teach and quiz tasks


