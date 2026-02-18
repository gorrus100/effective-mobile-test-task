# -slim - для уменьшения размера образа
# определённая версия Python, не latest
FROM python:3.10-slim AS builder

WORKDIR /app

# build-essential для компиляции возможных будущих зависимостей python
# netcat для healthcheck
# команды разбиты по разным строкам, так как применяется мультистейдж. оставшиеся кэши не повлияют на итоговый образ, но будет возможность добавлять другие зависимости без необходимости пересобирать предидущие 
RUN apt update 
RUN apt-get install -y build-essential 
RUN apt install netcat-openbsd

COPY requirements.txt .

# сначала скачиваются зависимости, потом копируется код, чтобы пересобирать в будущих сборках только src код
# --no-cache-dir для уменьшения размера образа
RUN pip install --no-cache-dir -r requirements.txt

# базовый образ соответсует базовому образу из предидущего сдейджа
FROM python:3.10-slim

WORKDIR /app
# передаём скачаные зависимости из предидущего сдейджа
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/bin/nc /usr/bin/nc
COPY . .

# запуск не от root 
RUN useradd python-app --no-create-home
USER python-app

# вывеска. порт может быть любым, указанным в .env
EXPOSE 8080 

# проверка сначала не сработает из-за имитации долгой загрузки. это будет использовано далее в docker-compose
HEALTHCHECK --interval=5s --timeout=1s --start-period=1s --retries=1 CMD [ "nc", "-z", "localhost", "8080" ]

# отсутствие переменных в dockerfile, прокидываются снаружи
CMD ["python", "app.py"]

