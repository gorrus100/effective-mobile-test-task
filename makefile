build_backend:
	docker build --tag app-python:1.0.0 backend

run_backend_alone:
	docker run  \
	-p 8080:7000 \
	--name app-python \
	--rm \
	--mount type=bind,src=.env,dst=/app/.env \
	app-python:1.0.0 