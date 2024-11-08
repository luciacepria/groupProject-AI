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

    @agent
    def recommender(self) -> Agent:
        return Agent(
        config = self.agents_config['recommender']
        )

    @agent
    def blogger(self) -> Agent:
        return Agent(
            config=self.agents_config['blogger']
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

    @task
    def recommender_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommender_task'],
            agent=self.recommender()
        )

    @task
    def blogger_task(self) -> Task:
        return Task(
            config=self.tasks_config['blogger_task'],
            agent=self.blogger()
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.accountant(),self.recommender(), self.blogger()],
            tasks=[self.researcher_task(), self.accountant_task(), self.recommender_task(), self.blogger_task()],
            process=Process.sequential,
            verbose=True
        )