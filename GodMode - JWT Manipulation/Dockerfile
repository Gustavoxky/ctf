FROM python:3.9-slim

WORKDIR /app
COPY app /app
RUN pip install flask pyjwt

EXPOSE 80
CMD ["python", "vulnerable_app_godmode.py"]
