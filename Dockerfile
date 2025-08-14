# syntax=docker/dockerfile:1

FROM python:3.11-slim

# Ensure non-root and predictable working dir
WORKDIR /app

# Install OS packages only if needed (uncomment and add if your project needs them)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential curl ca-certificates \
#   && rm -rf /var/lib/apt/lists/*

# Copy dependency files first to leverage Docker layer caching
# If the repo has requirements.txt or pyproject.toml, copy accordingly.
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . /app

# Default command runs the test suite
# You can pass extra pytest args at runtime: `docker run ... image pytest -q`
CMD ["pytest", "-q"]
