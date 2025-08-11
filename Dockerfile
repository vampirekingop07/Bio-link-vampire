FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "-m", "bot"]
