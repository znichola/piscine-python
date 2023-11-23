FROM python:3.12

# --no-cache-dir it's a docker thing, small image size and something about root user
RUN pip install --no-cache-dir \
    pylint \
    flake8 \
    tqdm \
    build

RUN apt-get update && apt-get install -y zsh

# Default powerline10k theme, no plugins installed
RUN  sh -c "$(curl -L https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t eastwood

RUN chsh -s /bin/zsh root
