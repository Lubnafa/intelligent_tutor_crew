from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class IntelligentTutorCrew():
    """IntelligentTutorCrew crew"""

    @agent
    def teacher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['teacher_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def quiz_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def grader_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['grader_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def feedback_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def teach_topic_task(self) -> Task:
        return Task(
            config=self.tasks_config['teach_topic_task'] # type: ignore[index]
        )

    @task
    def generate_quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_quiz_task'] # type: ignore[index]
        )

    @task
    def grade_answers_task(self) -> Task:
        return Task(
            config=self.tasks_config['grade_answers_task'] # type: ignore[index]
        )

    @task
    def provide_feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['provide_feedback_task'] # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

