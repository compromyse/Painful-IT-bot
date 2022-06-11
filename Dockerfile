# Use ubuntu image
FROM ubuntu:latest

# Change working directory to /painful_files
WORKDIR /painful_files

# Copy files
COPY . /painful_files

# Update system
RUN apt-get update

# Install discordpy dependencies
RUN apt-get install python3 python3-pip -y

# Install nmap
RUN apt-get install nmap -y

# Install discordpy
RUN python3 -m pip install -r requirements.txt

# Run bot
ENTRYPOINT ["python3", "/painful_files/main.py"]
