from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constant import WORK_DIR,TIMEOUT

def get_docker_executor():

    docker = DockerCommandLineCodeExecutor(
            # image = "python:3-slim", #use this image we can also put other image as we want
            work_dir=WORK_DIR,
            timeout=TIMEOUT, #seconds
        )
     
    return docker