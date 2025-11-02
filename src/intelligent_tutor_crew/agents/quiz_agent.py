"""Quiz Agent for generating quiz questions."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_quiz_agent() -> Agent:
    """Create and return the Quiz Agent."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.8)
    
    return Agent(
        role="Quiz Generator",
        goal="Create effective quiz questions that test understanding of the taught topic",
        backstory="""You are a curriculum developer specializing in assessment design. 
        You create clear, fair quiz questions that accurately measure student comprehension 
        and identify knowledge gaps.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


QuizAgent = create_quiz_agent()

