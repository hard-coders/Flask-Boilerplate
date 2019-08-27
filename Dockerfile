FROM python:3.7-alpine

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY . /usr/src/app
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]