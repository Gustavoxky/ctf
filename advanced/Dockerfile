FROM python:3.9-slim

WORKDIR /app
COPY app /app
COPY flag.txt /app/flag.txt

RUN pip install flask

EXPOSE 80
CMD ["python", "vulnerable_app_advanced.py"]
