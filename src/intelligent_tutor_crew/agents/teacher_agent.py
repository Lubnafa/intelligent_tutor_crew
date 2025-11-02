"""Teacher Agent for explaining topics to students."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_teacher_agent() -> Agent:
    """Create and return the Teacher Agent."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
    
    return Agent(
        role="Educational Teacher",
        goal="Explain programming and computer science topics clearly and comprehensively",
        backstory="""You are an experienced educator with a passion for making complex 
        concepts accessible. You break down topics into digestible steps and use practical 
        examples to help students understand.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


TeacherAgent = create_teacher_agent()

