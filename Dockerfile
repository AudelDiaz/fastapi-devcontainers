FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 8000
RUN apt update && apt -y install git fish 
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && pip install black
COPY . /app
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser
WORKDIR /app/src
CMD sleep infinity
