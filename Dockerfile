FROM ubuntu:latest

WORKDIR /heroku

RUN chmod 777 /run_web.sh
RUN chmod -R 777 /main
RUN chmod -R 777 ./

ENV PORT=80
EXPOSE $PORT

ENTRYPOINT ["./run_web.sh"]
