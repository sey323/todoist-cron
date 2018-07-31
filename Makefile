NAME=thor

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_thor_1
	docker rm -f ${NAME}_thor_1
