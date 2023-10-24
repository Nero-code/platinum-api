FROM python:3.9-slim

# Create working folder and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application contents
COPY . .

# Switch to a non-root user
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

# Run the service
EXPOSE 5000
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--log-level=info", "service:app"]
