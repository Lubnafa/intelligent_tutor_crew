# Intelligent Tutor Crew

An intelligent AI tutoring system built with CrewAI that teaches, quizzes, grades, and provides feedback on programming and computer science concepts using Google's Gemini models.

## 🏗️ Project Structure

This project follows the official CrewAI project structure:

```
intelligent_tutor_crew/
├── src/
│   └── intelligent_tutor_crew/    # Main package
│       ├── __init__.py
│       ├── crew.py                 # Crew assembly
│       ├── main.py                 # Package entry point
│       ├── agents/                 # Agent definitions
│       │   ├── __init__.py
│       │   ├── teacher_agent.py
│       │   ├── quiz_agent.py
│       │   ├── grader_agent.py
│       │   └── feedback_agent.py
│       ├── tasks/                  # Task definitions
│       │   ├── __init__.py
│       │   ├── teach_task.py
│       │   ├── quiz_task.py
│       │   ├── grade_task.py
│       │   └── feedback_task.py
│       ├── tools/                  # Custom tools
│       │   └── __init__.py
│       └── config/                 # Configuration files
│           ├── agents.yaml         # Agent definitions (YAML)
│           └── tasks.yaml          # Task definitions (YAML)
├── tests/                          # Test files
│   ├── __init__.py
│   └── test_crew.py
├── data/                           # Data directory
│   ├── input/                      # Input data
│   └── output/                     # Output data
├── outputs/                        # CrewAI outputs
├── main.py                         # Root entry point (convenience)
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project configuration
├── .env.example                    # Environment variables template
└── README.md                       # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd intelligent_tutor_crew
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

### Usage

Run the main application:

```bash
python main.py
```

You can modify `main.py` to:
- Accept command-line arguments for topics
- Accept student answers for grading
- Read topics from files
- Customize the crew workflow

## 🤖 Agents

The crew consists of four specialized agents:

1. **TeacherAgent**: Explains topics step-by-step with examples
2. **QuizAgent**: Generates quiz questions based on the topic
3. **GraderAgent**: Evaluates student answers and provides scores
4. **FeedbackAgent**: Summarizes performance and recommends improvements

## 📝 Tasks

The crew executes tasks sequentially:

1. **Teach Topic**: Provides comprehensive topic explanation
2. **Generate Quiz**: Creates quiz questions based on the explanation
3. **Grade Answers**: (Optional) Grades student responses
4. **Provide Feedback**: (Optional) Generates personalized feedback

## 🔧 Configuration

- **Python-based**: Modify agent and task files in `src/intelligent_tutor_crew/agents/` and `src/intelligent_tutor_crew/tasks/`
- **YAML-based**: Use `src/intelligent_tutor_crew/config/agents.yaml` and `src/intelligent_tutor_crew/config/tasks.yaml` for declarative configuration

## 📦 Dependencies

- `crewai`: Multi-agent framework
- `google-generativeai`: Gemini API integration
- `python-dotenv`: Environment variable management
- `langchain-google-genai`: LangChain integration for Gemini
- `pydantic`: Data validation
- `rich`: Enhanced terminal output

## 🎯 Example Usage

```python
from src.intelligent_tutor_crew.crew import create_intelligent_tutor_crew

# Create crew for a topic
crew = create_intelligent_tutor_crew(topic="Python decorators")

# Run the crew
result = crew.kickoff()
print(result)
```

Or run from the command line:
```bash
# Using root main.py
python main.py

# Or using package main.py
python -m src.intelligent_tutor_crew.main
```

## 📄 License

This project is part of a learning application and can be used for educational purposes.

## 🤝 Contributing

Feel free to extend this project with additional agents, tasks, or tools to enhance the tutoring experience!

