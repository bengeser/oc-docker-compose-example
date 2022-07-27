# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

LABEL org.opencontainers.image.title "Meine Python App"
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY hello_world.py /app

LABEL org.opencontainers.image.version "1.0"
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Normaler weg: CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.hello_world:app"]
CMD ["python", "hello_world.py"]
