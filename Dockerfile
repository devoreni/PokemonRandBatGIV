# Use the LATEST stable, long-term support version of Ubuntu.
# This ensures access to modern packages like python3-pyqt6.
FROM ubuntu:24.04

# Set an environment variable to prevent interactive prompts during installation.
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory inside the container.
WORKDIR /app

# Install Python 3, pip, and the SYSTEM version of PyQt6.
# The `python3-pyqt6` package in Ubuntu 24.04's repositories correctly
# installs PyQt6 and ALL of its required system dependencies.
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-pyqt6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the (modified) requirements.txt file.
COPY requirements.txt .

# Use the installed pip to install the rest of our Python dependencies.
# We use `python3 -m pip` to ensure we're using the correct pip.
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of our project code.
COPY . .

# Set the default command, using the standard `python3` executable.
CMD ["python3", "pokemon_dml.py"]