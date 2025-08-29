async def start_docker_container(docker):
    print("Docker Starting.")
    await docker.start()
    print("Docker Started.")

async def stop_docker_container(docker):
    print("Docker Stopping.")
    await docker.stop()
    print("Docker Stopped.")