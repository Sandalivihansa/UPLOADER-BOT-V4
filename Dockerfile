FROM python:3.10-slim

WORKDIR /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg git wget pv jq python3-dev mediainfo && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install the required packages from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt --verbose

# Additional steps as necessary...
COPY . .

CMD ["python3", "bot.py"]
