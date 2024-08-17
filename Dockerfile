FROM python:3.11-slim
WORKDIR /app
COPY . parser1.py /app/
ENTRYPOINT [ "python", "parser1" ]



