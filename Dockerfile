# Use Python 3.6 or later as a base image
FROM python:latest
# Copy contents into image
COPY . .
# Install pip dependencies from requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "main.py"]
