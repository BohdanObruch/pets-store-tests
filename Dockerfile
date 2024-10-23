# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry and dependencies
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Set environment variable
ARG PROD
ENV PROD=$PROD

# Run pytest when the container launches
CMD ["poetry", "run", "pytest", "--alluredir=allure-results"]