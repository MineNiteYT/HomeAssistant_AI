FROM python:3.11-slim
WORKDIR /app
COPY run.py /app/run.py
RUN pip install flask requests
CMD ["python", "run.py"]
