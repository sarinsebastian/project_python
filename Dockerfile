FROM python:3.11-slim
WORKDIR /app
COPY . /app/
ENTRYPOINT [ "python", "parser1.py" ]



