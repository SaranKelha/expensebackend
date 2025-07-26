# Start from an official Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app2


# Copy the contents of your local "app" folder into the container's /app folder
COPY . .

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt



# Command to run the application using uvicorn
# We use 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]