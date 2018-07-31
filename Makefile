NAME=thor

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_loki_1
	docker rm -f ${NAME}_loki_1
