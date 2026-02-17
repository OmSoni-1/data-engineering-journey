# Use official Python image
FROM python: 3.11-slim

# Set working directory
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]