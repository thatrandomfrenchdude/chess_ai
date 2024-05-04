# Chess AI
This repo contains my own personal chess tooling and other code. The latest version is based around the Stockfish chess engine.

### Purpose
The purpose of this AI is to provide me with a platform to run chess experiments so that I can better learn how to play chess.

I am designing some AI bots w/ various capabilities that play chess differently, and I also plan to include some framework for testing genetic AI algorithms.

At the moment this game is command line only, but I have tentative plans to add a basic react ui that can be watched.

### Status
This code plays two AI BestBots against each other. An AI BestBot always chooses the best move according to the stockfish engine.

### Run Tests
```./scripts/test.sh```

### Run Code
```./scripts/run.sh```

### Move Format
Moves should be formated using lowercase letters with no spaces (Ex: e2e4)