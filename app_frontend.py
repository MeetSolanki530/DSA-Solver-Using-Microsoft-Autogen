import streamlit as st
from teams.dsa_team import create_dsa_team
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage
import asyncio

st.title("DSASolver - DSA Solver Application")

st.write("Welcome to DSASolver! Your Personal DSA Solver Assistant.")

user_input = st.text_area("Please Enter Your DSA Problem or Question:",value="write a code to add two numbers")

async def solve_dsa_problem(team,docker,task: str):
    dsa_team,docker = create_dsa_team()
    try:
        await start_docker_container(docker)

        async for message in dsa_team.run_stream(task=task):
            
            if isinstance(message,TextMessage):
                print(f"{message.source} : {message.content}")
                yield message

            elif isinstance(message,TaskResult):
                print(f"Stop Reason: {message.stop_reason}")
                yield message

    except Exception as e:
        st.write(f"Error occurred: {e}")
    finally:
        await stop_docker_container(docker)

if st.button("Solve DSA Problem"):
    if user_input:


        team,docker = create_dsa_team()

        st.markdown("Solving your DSA problem...")

        async def collect_messages():

            async for message in solve_dsa_problem(team,docker,user_input):
                
                if isinstance(message, TextMessage):
                    if message.source == "user":
                        with st.chat_message("user", avatar="🧑‍💻"):
                            st.markdown(f"User :- {message.content}")

                    elif message.source == "DSA_Problem_Solver_Agent":
                        with st.chat_message("assistant", avatar="🤖"):
                            st.markdown(f"DSA Solver :- {message.content}")

                    elif message.source == "code_executor_agent":
                        with st.chat_message("assistant", avatar="💻"):
                            st.markdown(f"Code Executor :- {message.content}")

                    else:
                        with st.chat_message("assistant", avatar="📢"):
                            st.markdown(f"{message.source}: {message.content}")
                
                 # Handle stop result once (no duplicates)
                elif isinstance(message, TaskResult):
                    with st.chat_message("stopper", avatar="🚫"):
                        st.markdown(f"Stop Reason: {message.stop_reason}")
  
    asyncio.run(collect_messages())
