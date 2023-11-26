# 
FROM python:3.10-slim-bullseye

# Setup working directory
WORKDIR /app
# Copy all files in directory
COPY . ./
# Run pip install
RUN pip install --no-cache-dir -r requirements.txt
# Spin up application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]