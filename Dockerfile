FROM python:3.12-slim

WORKDIR /app

# Copy application files
COPY index.html server.py ./

# Expose the port the server runs on
EXPOSE 8000

# Run the server when the container starts
CMD ["python3", "server.py"]
