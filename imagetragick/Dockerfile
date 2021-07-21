FROM        centos:7
MAINTAINER  SEC

# Install packages
RUN         yum install epel-release -y
RUN         yum install python-pip3 python3 ImageMagick-6.7.8.9-10.el7 nmap-ncat -y
RUN python3 --version

ADD	    proof.txt /root/proof.txt
COPY        ./app /app
WORKDIR     /app
RUN 		pip3 install setuptools -U
# Install pip modules
RUN         pip3 install -r requirements.txt

EXPOSE      8080

CMD         python app.py
