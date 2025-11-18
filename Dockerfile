# Stage 1: Build stage
FROM python:3.9-slim AS builder

WORKDIR /app
COPY app.py .

# Install dependencies (none here, but kept for future)
RUN pip install --no-cache-dir argparse

# Stage 2: Runtime stage
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /app /app

ENTRYPOINT ["python", "app.py"]
