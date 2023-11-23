# FROM ubuntu:latest
FROM alpine:latest

ENV SOURCE_REPO https://github.com/official-stockfish/Stockfish/archive/refs/tags/sf_16.tar.gz

ADD ${SOURCE_REPO} /root

WORKDIR /root

# build and install stockfish from source
RUN tar xvzf *.tar.gz \
    && apk add --update --no-cache make g++ \
    && cd Stockfish-sf_16/src \
    # && make build ARCH=x86-64-modern \
    && make build ARCH=armv8 \
    && make install \
    && cd ../.. \
    && rm -rf Stockfish-sf_16 *.tar.gz

# RUN apt-get install stockfish

ENV PYTHONUNBUFFERED=1

# Install Python and necessary dependencies
RUN apk add --update --no-cache python3 \
    && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools \
    && pip install pytest python-chess stockfish

COPY . .

# ENV PATH="${PATH}:stockfish16/stockfish"

ENTRYPOINT ["python", "test.py"]
# # ENTRYPOINT ["pytest", "-v", "--color=yes", "test.py"]
# ENTRYPOINT ["python", "test.py"]
# # ENTRYPOINT [ "/usr/local/bin/stockfish" ] # use to run stockfish directly
