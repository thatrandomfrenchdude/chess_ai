RUN_DOCKER_TESTS = False

def run_sys_command(cmd):
    import subprocess
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode("utf-8")

def test_docker():
    if RUN_DOCKER_TESTS:
        print(run_sys_command("pwd"))
        print(run_sys_command("ls -lrt"))
        print(run_sys_command("ls -lrt /app/src"))
    assert True

# tests that the main game loop runs with two AI BestBot entities
def test_chess_game():
    from src.chessGame.autochess import AutoChess
    # game parameters
    params = {
        'testing': True,
        'docker': True,
    }
    
    game = AutoChess(params=params)
    game.loop()
    assert True

if __name__ == "__main__":
    test_docker()
    test_chess_game()