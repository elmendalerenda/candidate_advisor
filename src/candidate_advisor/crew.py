from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import BraveSearchTool, ScrapeWebsiteTool, FileReadTool
from crewai_tools import SeleniumScrapingTool
from crewai_tools import FileReadTool




# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CandidateAdvisor():
	"""CandidateAdvisor crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	#@agent
	#def researcher(self) -> Agent:
	#	return Agent(
	#		config=self.agents_config['researcher'],
	#		verbose=True,
	#		tools=[BraveSearchTool()]
	#	)

	#@agent
	#def reporting_analyst(self) -> Agent:
	#	return Agent(
	#		config=self.agents_config['reporting_analyst'],
	#		verbose=True
	#	)
	
	@agent
	def job_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['job_researcher'],
			verbose=True
		)
	
	@agent
	def candidate_success(self) -> Agent:
		return Agent(
			config=self.agents_config['candidate_success'],
			verbose=True
		)
	
	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			verbose=True
		)
	
	@agent
	def interview_coach(self) -> Agent:
		return Agent(
			config=self.agents_config['interview_coach'],
			verbose=True
		)
	
	@agent
	def strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['strategist'],
			verbose=True
		)
	
	@agent
	def industry(self) -> Agent:
		return Agent(
			config=self.agents_config['industry'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	#@task
	#def research_task(self) -> Task:
	#	return Task(
	#		config=self.tasks_config['research_task'],
	#	)

	#@task
	#def reporting_task(self) -> Task:
	#	return Task(
	#		config=self.tasks_config['reporting_task'],
	#		output_file='report.md'
	#	)
	
	@task
	def job_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['job_research_task'],
			output_file='research.md',
			tools=[BraveSearchTool(), ScrapeWebsiteTool(), FileReadTool()]
		)
	
	@task
	def candidate_task(self) -> Task:
		return Task(
	 		config=self.tasks_config['candidate_task'],
			output_file='candidate.md',
	 		tools=[BraveSearchTool(), ScrapeWebsiteTool(), FileReadTool(file_path='resume.md'), FileReadTool(file_path='profile.txt')]
	 	)
	
	@task
	def writer_task(self) -> Task:
	 	return Task(
	 		config=self.tasks_config['writer_task'],
	 		output_file='improved_resume.md',
	 		tools=[BraveSearchTool(), ScrapeWebsiteTool(), FileReadTool(file_path='resume.md')]
	 	)
	
	@task
	def interview_task(self) -> Task:
		return Task(
	 		config=self.tasks_config['interview_task'],
	 		output_file='interview.md',
	 		tools=[BraveSearchTool(), ScrapeWebsiteTool()]
	 	)
	
	@task
	def strategy_task(self) -> Task:
	 	return Task(
	 		config=self.tasks_config['strategy_task'],
	 		output_file='strategy.md'
	 	)
	
	@task
	def industry_task(self) -> Task:
	 	return Task(
	 		config=self.tasks_config['industry_task'],
	 		output_file='industry.md',
	 		tools=[
	 			BraveSearchTool(), ScrapeWebsiteTool()
	 		]
	 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the CandidateAdvisor crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
