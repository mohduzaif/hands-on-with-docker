# Base Image
FROM python:3.13-slim

# Working Directory
WORKDIR /app 

# Copy requirements file
COPY requirements.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy all project files
COPY . .

# Expose the PORT
EXPOSE 8000

# Write FastAPI Application CMD in the list
CMD ["uvicorn", "app:app1", "--host", "0.0.0.0", "--port", "8000"]