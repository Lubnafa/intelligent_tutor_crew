"""Grader Agent for evaluating student answers."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_grader_agent() -> Agent:
    """Create and return the Grader Agent."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    
    return Agent(
        role="Answer Grader",
        goal="Evaluate student answers accurately and provide constructive feedback",
        backstory="""You are a fair and thorough grader who provides detailed feedback 
        on student responses. You identify both correct and incorrect answers, explaining 
        mistakes to help students learn.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


GraderAgent = create_grader_agent()

