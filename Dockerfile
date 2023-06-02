#### Python3.8
FROM python:3.8.10-slim-buster AS builder

# Working Directory
WORKDIR /app
COPY requirements.txt .

# Install packages from requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

CMD ["/bin/bash"]

#### Ubuntu 20.04 + Python3.8 
# FROM ubuntu:20.04
# WORKDIR /app
# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install -y python3.8 python3-pip python-dev build-essential
# RUN pip3 install -r requirements.txt
# ENTRYPOINT [ "/bin/bash" ]