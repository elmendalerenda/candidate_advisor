# CandidateAdvisor Crew

Welcome to the CandidateAdvisor Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**
**Add your `BRAVE_API_KEY` into the `.env` file**

## Running the Project

The agents need 3 `.md` text files in the root folder:

 - job_offer.md that contains the job offer.
 - resume.md containing the candidate resume
 - profile.md containing an extended candidate profile

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the candidate-advisor Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The candidate-advisor Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CandidateAdvisor Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)