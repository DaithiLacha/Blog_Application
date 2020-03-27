FROM jenkins/jenkins:lts
USER root
RUN apt-get update
RUN curl -sSL https://get.docker.com/ | sh
FROM ubuntu:latest
MAINTAINER David O Connor "david.oc4096@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /Blog_Application
WORKDIR /Blog_Application
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_blog.py"]
