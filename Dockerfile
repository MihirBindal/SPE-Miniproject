# 1. Use an official, lightweight Python image as our base
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy everything from your local folder into the container's /app folder
COPY . /app

# 4. Install the required dependencies (like pytest)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Keep the container alive in the background
CMD ["tail", "-f", "/dev/null"]
