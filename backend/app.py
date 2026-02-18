
from flask import Flask
from dotenv import load_dotenv
from os import environ
from sys import exit
from time import sleep

load_dotenv()
port=environ.get("APP_PORT")
has_delay=environ.get("APP_HAS_DELAY", "false").lower() == "true"
delay=5
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
    return root_answer

if has_delay:
    print("##########################################################################################") 
    print(f"### Искусственная задержка долгого старта приложения({delay} секунд). Для healthcheck... #######")
    print("##########################################################################################", flush=True ) 
    sleep(delay)  # имитация долгой загрузки приложения для healthcheck

app.run(host="0.0.0.0", port=port_value)