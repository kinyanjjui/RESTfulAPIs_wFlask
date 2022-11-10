#Using lightweight debian image
FROM python:3.10-slim-bullseye

#Installing packages
RUN pip install --no-cache-dir pipenv

#Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY main ./main

#Install API dependencies
RUN pipenv install --system --deploy

#start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]

