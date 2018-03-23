# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# We're using pipenv to manage dependencies
RUN pip install "pipenv>=8.2,<8.3"

# Make port 80 available to the world outside this container
#EXPOSE 8080

# Define environment variable
#ENV NAME HelloFlask

# Install all deps
RUN pipenv install --system


# Show dependency graph
#RUN pipenv graph

# Check packages are safe
#RUN pipenv check


# Run app.py when the container launches
CMD ["python", "app.py"]
