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

# Create staticfiles directory (optional but good practice)
RUN mkdir -p /app/staticfiles

# Collect static files during build
# We set a dummy SECRET_KEY if none exists to avoid Django errors
RUN SECRET_KEY=dummy python manage.py collectstatic --noinput

# EXPOSE the port Render uses
EXPOSE 10000

# Run the application using Gunicorn, but run migrations and admin setup first
CMD ["sh", "-c", "python manage.py migrate && python create_admin.py && gunicorn --bind 0.0.0.0:10000 mysite.wsgi:application"]
