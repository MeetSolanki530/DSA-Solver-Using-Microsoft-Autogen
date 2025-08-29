from autogen_agentchat.teams import RoundRobinGroupChat
from agents.code_executor import get_code_executor_agent
from agents.problem_solver import get_problem_solver_agent
from config.constant import TEXT_MENTION,MAX_TURNS
from autogen_agentchat.conditions import TextMentionTermination

def create_dsa_team():
    problem_solver_agent = get_problem_solver_agent()
    code_executor_agent,docker = get_code_executor_agent()
    team = RoundRobinGroupChat(
        participants=[problem_solver_agent,code_executor_agent],
        termination_condition=TextMentionTermination(TEXT_MENTION),
        max_turns=MAX_TURNS,
        description="A team of agents to solve DSA problems. Always Use code_executor_agent to run code before responding to user raw code.",
        name="DSA_Team"
    )

    return team,docker