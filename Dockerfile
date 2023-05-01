# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Run the command to collect static files
RUN python manage.py collectstatic --noinput

# Set entrypoint command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
