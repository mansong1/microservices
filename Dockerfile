FROM python:3.12.0b1

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy application
COPY . /usr/src/app

# run server
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]
