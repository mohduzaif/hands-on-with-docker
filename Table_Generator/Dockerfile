# Base Image
FROM python:3.11-slim

# Working Directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt 

# Copy project file
COPY . .

# Expose Flask port 
EXPOSE 5000

# Run Application
CMD ["python", "app.py"]