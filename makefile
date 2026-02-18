include .env
export

build_backend:
	docker build --tag app-python:1.0.0 backend

run_backend_alone:
	docker run  \
	-p ${APP_PORT}:${APP_PORT} \
	--name app-python \
	--env-file .env \
	--rm \
	--mount type=bind,src=.env,dst=/app/.env \
	app-python:1.0.0 
