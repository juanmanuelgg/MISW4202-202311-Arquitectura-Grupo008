FROM python:3.9.16-slim-buster

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt
# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

ENV FLASK_APP=flaskr/app.py
# Start the application
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]