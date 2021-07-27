FROM ubuntu:latest

WORKDIR /heroku/main

RUN chmod 777 /heroku/main/run_web.sh
RUN chmod -R 777 /main
RUN chmod -R 777 ./

ENV PORT=80
EXPOSE $PORT

ENTRYPOINT ["./run_web.sh"]
