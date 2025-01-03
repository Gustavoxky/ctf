FROM python:3.9-slim

WORKDIR /app
COPY app /app
RUN pip install flask requests

EXPOSE 80
CMD ["python", "vulnerable_app_expert.py"]
