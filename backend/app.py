
from flask import Flask, request
from os import environ
from sys import exit
from time import sleep

port=environ.get("APP_PORT")
has_delay=environ.get("APP_HAS_DELAY", "false").lower() == "true"
delay=2
root_answer = "Hello from Effective Mobile!\n"

# порт обязательно должен быть указан в .env
try:
    port_value = int(port)
except (TypeError, ValueError):
    print(f"APP_PORT должeн быть указан в .env и быть числом, получено: {port}")
    exit(1)

app = Flask(__name__)

@app.route('/')
def root():
    # смотрим заголовки которые пришли из nginx
    headers = request.headers
    # Фильтруем только X-* которые явно задали
    x_headers = {k: v for k, v in headers.items() if k.startswith("X-")}
    print(f"headers from NGINX ->  {x_headers}", flush=True)
    return root_answer

if has_delay:
    print("##########################################################################################") 
    print(f"### Искусственная задержка долгого старта приложения({delay} секунды). Для healthcheck... ######")
    print("##########################################################################################", flush=True ) 
    sleep(delay)  # имитация долгой загрузки приложения для healthcheck

app.run(host="0.0.0.0", port=port_value)