FROM ubuntu:latest

ADD . /heroku/main/

RUN chmod 777 ./heroku/main/run_web.sh
#RUN chmod -R 777 ./main
#RUN chmod -R 777 ./

ENV PORT=80
EXPOSE $PORT

WORKDIR /heroku/main

ENTRYPOINT ["./run_web.sh"]
