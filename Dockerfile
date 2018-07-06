FROM python:2.7

WORKDIR /app

# Copy the current directory contents
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app/manipulate/create-db.py"]
