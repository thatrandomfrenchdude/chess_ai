from game.autochess import AutoChess


def app() -> None:
    game = AutoChess()
    game.loop()


if __name__ == '__main__':
    app()