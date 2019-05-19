NAME=loki

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_cron_1
	docker rm -f ${NAME}_cron_1

in:
	docker exec -it ${NAME}_cron_1 /bin/bash
