# Use official Python 3.11 slim image
FROM python:3.11-slim

# Environment setup
ENV POETRY_VERSION=1.8.2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y curl build-essential && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy Poetry config first to install dependencies (cached layer)
COPY test-messenger/pyproject.toml test-messenger/poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# Copy the rest of the app code
COPY test-messenger/ /app/

# Expose the app port
EXPOSE 8000

# Start FastAPI app via Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
