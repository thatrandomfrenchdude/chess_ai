RUN_DOCKER_TESTS = False

def run_sys_command(cmd):
    import subprocess
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode("utf-8")

if RUN_DOCKER_TESTS:
    import os
    print(os.getcwd())
    print(run_sys_command("ls -lrt"))

from game import Chess

# tests that the main game loop runs with two AI BestBot entities
def test_chess_game():
    # game parameters
    params = {
        'testing': True,
        'docker': True,
    }
    
    game = Chess(params=params)
    game.loop()
    assert True