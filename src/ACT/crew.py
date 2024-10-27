from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ACTCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def _init_(self) -> None:
        pass

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher']
        )

    @agent
    def accountant(self) -> Agent:
        return Agent(
            config=self.agents_config['accountant']
        )

    @task
    def researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['researcher_task'],
            agent=self.researcher()
        )

    @task
    def accountant_task(self) -> Task:
        return Task(
            config=self.tasks_config['accountant_task'],
            agent=self.accountant()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.accountant()],
            tasks=[self.researcher_task(), self.accountant_task()],
            process=Process.sequential,
            verbose=True
        )