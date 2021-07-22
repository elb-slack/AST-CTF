FROM        centos:7
MAINTAINER  SEC

RUN         yum install epel-release -y
RUN         yum groupinstall "Development Tools" -y
RUN         yum install python-pip3 python3 nmap-ncat -y
RUN         yum install ghostscript-devel libpng-devel libxml2-devel -y

COPY        ImageMagick-6.9.1-10.tar.gz ImageMagick-6.9.1-10.tar.gz
RUN         tar -xvzf ImageMagick-6.9.1-10.tar.gz
RUN         cd ImageMagick-6.9.1-10 && ./configure --with-gslib --with-libpng --with-zlib=yes --with-xml=yes && make && make install

RUN         ldconfig /usr/local/lib


ADD         proof.txt /root/proof.txt
COPY        ./app /app
WORKDIR     /app


RUN         pip3 install setuptools -U
RUN         pip3 install git+https://github.com/maxcountryman/flask-uploads.git
RUN         pip3 install -r requirements.txt

EXPOSE      8080


