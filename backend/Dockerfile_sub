# Use official lightweight Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements.txt initially to utilize Docker cache efficiently
COPY requirements.txt .

# Upgrade pip and install dependencies from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the backend source code into the container
COPY . .

# Expose port 5000 (common for Flask apps)
EXPOSE 5000

# Command to run your subscriber Python script (adjust if you run a web server)
CMD ["python", "subscriber.py"]
