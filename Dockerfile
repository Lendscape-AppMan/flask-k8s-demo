FROM python:3.8-slim

# Install dependencies
RUN python -m pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Create app directory
WORKDIR /app

# Copy app files
COPY app.py /app/app.py
COPY test_app.py /app/test_app.py
COPY database.db /app/database.db
COPY templates/ /app/templates/

# Expose port for Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
