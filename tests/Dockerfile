FROM alpine:3.18

ENV ENGINE_REPO https://github.com/official-stockfish/Stockfish/archive/refs/tags/sf_16.tar.gz

WORKDIR /app

ADD ${ENGINE_REPO} .

# build and install stockfish from source
RUN tar xvzf *.tar.gz \
    && apk add --update --no-cache make g++ \
    && cd Stockfish-sf_16/src \
    && make build ARCH=armv8 \
    && make install \
    && cd ../.. \
    && rm -rf Stockfish-sf_16 *.tar.gz

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install Python and necessary dependencies
RUN apk add --update --no-cache python3 poetry \
    && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools

# install python packages poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY src /app/src
COPY tests /app/tests

ENTRYPOINT ["pytest", "-v", "--color=yes", "tests/test.py"]