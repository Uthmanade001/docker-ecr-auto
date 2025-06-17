# Use official Python image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Run the app
CMD ["python", "app.py"]
