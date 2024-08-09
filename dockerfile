FROM python:slim

RUN pip install numpy

RUN pip install matplotlib

RUN pip install pandas

RUN apt -y update && apt -y install git

WORKDIR /mnt
