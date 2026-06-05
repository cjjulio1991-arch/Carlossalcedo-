FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 3000

CMD ["python3", "-m", "nexus6.api.main"]
