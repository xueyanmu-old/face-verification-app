FROM ubuntu:21.04
ARG DEBIAN_FRONTEND=noninteractive

# Install OpenJDK 8
RUN \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y dos2unix && \
    apt-get install -y python3 python3-dev python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_FORMAT=legacy

RUN apt-get -y update && apt-get install -y --fix-missing libzbar-dev bash gcc git libc-dev

RUN apt-get install -y netcat && apt-get autoremove -y

RUN apt-get install -y build-essential
RUN pip3 install deepface==0.0.65


COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt
RUN pip3 uninstall keras -y
RUN pip3 install keras==2.4.3

RUN mkdir -p /main

#gennaro's addition to find run_web.sh
ADD . /heroku/main/

WORKDIR /heroku/main

RUN chmod 777 ./heroku/main/run_web.sh
RUN chmod -R 777 ./heroku/main
#RUN chmod -R 777 ./
RUN dos2unix ./heroku/main/run_web.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

ENV PORT=80
EXPOSE $PORT

ENTRYPOINT ["./heroku/main/run_web.sh"]
