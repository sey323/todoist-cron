FROM python:latest

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install oauth2client requests pytodoist slacker slackbot todoist-python schedule

# cron設定ファイルの移動
ADD todoist-cron /etc/cron.d/todoist-cron
RUN chmod 0644 /etc/cron.d/todoist-cron

ADD ./cron /cron
ADD ./config.json /

ADD ./init.sh /init.sh
RUN chmod -R +x /init.sh
RUN /init.sh

RUN apt-get install -y cron

COPY ./todoist-cron ./todoist-cron
RUN crontab todoist-cron

CMD cron -f
