FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY publisher.py .
COPY creds ./creds 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 6000
CMD ["python", "publisher.py"]