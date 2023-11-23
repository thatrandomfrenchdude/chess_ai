RUN_DOCKER_TESTS = True

def run_sys_command(cmd):
    import subprocess
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode("utf-8")

if RUN_DOCKER_TESTS:
    import os
    print(os.getcwd())
    print(run_sys_command("ls -lrt"))
    print(run_sys_command("ls -lrt stockfish16"))
    print(run_sys_command("which stockfish"))
    print(run_sys_command("stockfish --version"))

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

if __name__ == "__main__":
    test_chess_game()