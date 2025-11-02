"""Feedback Agent for providing learning summaries."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_feedback_agent() -> Agent:
    """Create and return the Feedback Agent."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)
    
    return Agent(
        role="Learning Feedback Provider",
        goal="Summarize student performance and provide actionable improvement recommendations",
        backstory="""You are a learning coach who analyzes student performance holistically. 
        You identify strengths, weaknesses, and provide clear guidance on how to improve 
        understanding of the topic.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


FeedbackAgent = create_feedback_agent()

