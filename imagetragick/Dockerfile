FROM        centos:7
MAINTAINER  SEC

# Install packages
RUN         yum install epel-release -y
RUN yum groupinstall "Development Tools" -y
RUN         yum install python-pip3 python3 nmap-ncat -y


COPY ImageMagick-6.9.1-10.tar.gz ImageMagick-6.9.1-10.tar.gz
RUN tar -xvzf ImageMagick-6.9.1-10.tar.gz
RUN cd ImageMagick-6.9.1-10 && ./configure && make && make install

ADD	    proof.txt /root/proof.txt
COPY        ./app /app
WORKDIR     /app
RUN 		pip3 install setuptools -U
# Install pip modules
RUN         pip3 install -r requirements.txt

EXPOSE      8080


