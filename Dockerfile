# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# EXPOSE the port Render uses (can be anything, Render binds to what you EXPOSE)
EXPOSE 10000

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "mysite.wsgi:application"]
