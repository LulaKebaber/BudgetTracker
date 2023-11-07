FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /code
COPY . /code/

# Expose the port that the app will run on
EXPOSE 8000

# Define the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
