import asyncio
from teams.dsa_team import create_dsa_team
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

async def main(task:str):
    dsa_team,docker = create_dsa_team()
    try:
        await start_docker_container(docker)

        async for message in dsa_team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print('=='*20)
                print(message.source," : ",message.content)
                print('=='*20)
            elif isinstance(message,TaskResult):
                print("Stop Reason:",message.stop_reason)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await stop_docker_container(docker)

if __name__ == "__main__":
    asyncio.run(main("Write python code to add two numbers."))