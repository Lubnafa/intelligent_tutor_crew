"""Crew definition for the Intelligent Tutor Crew."""

from crewai import Crew, Process
from .agents import TeacherAgent, QuizAgent, GraderAgent, FeedbackAgent
from .tasks import (
    teach_topic_task,
    generate_quiz_task,
    grade_answers_task,
    provide_feedback_task,
)


def create_intelligent_tutor_crew(topic: str, student_answers: str = None) -> Crew:
    """Create and configure the Intelligent Tutor Crew."""
    
    # Create tasks with dependencies
    teach_task = teach_topic_task(topic)
    
    quiz_task = generate_quiz_task("{{teach_topic_task.output}}")
    quiz_task.context = [teach_task]
    
    # If student answers provided, create grading and feedback tasks
    if student_answers:
        grade_task = grade_answers_task(
            "{{generate_quiz_task.output}}",
            student_answers
        )
        grade_task.context = [quiz_task]
        
        feedback_task = provide_feedback_task(
            "{{grade_answers_task.output}}",
            topic
        )
        feedback_task.context = [grade_task]
        
        tasks = [teach_task, quiz_task, grade_task, feedback_task]
    else:
        # If no answers, just teach and create quiz
        tasks = [teach_task, quiz_task]
    
    # Create and return crew
    return Crew(
        agents=[TeacherAgent, QuizAgent, GraderAgent, FeedbackAgent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

