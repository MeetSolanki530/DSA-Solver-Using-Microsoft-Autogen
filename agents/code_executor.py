from autogen_agentchat.agents import CodeExecutorAgent,AssistantAgent
from config.docker_executor import get_docker_executor

def get_code_executor_agent():
    """
    Get the DSA Code Executor Agent.
    """
    docker = get_docker_executor()

    code_executer_agent = CodeExecutorAgent(
        name = "code_executor_agent",
        code_executor=docker,
        description="An Agent who Execute Given Code of Python. Always Use this to run code before responding to user."
    )

    return code_executer_agent,docker