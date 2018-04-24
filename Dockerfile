FROM python:latest

RUN pip install --upgrade pip
RUN pip install oauth2client requests pytodoist slacker slackbot todoist-python schedule

RUN apt-get update
RUN apt-get install -y cron

# cron設定ファイルの移動
ADD todoist-cron /etc/cron.d/todoist-cron
RUN chmod 0644 /etc/cron.d/todoist-cron

ADD ./cron /cron
ADD ./config.json /

ADD ./scripts /scripts
RUN chmod -R +x /scripts

#CMD cron && touch /etc/cron.d/simple-cron && tail -f /dev/null
CMD /scripts/init.sh
