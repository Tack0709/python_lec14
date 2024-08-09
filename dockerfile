FROM python:slim

RUN pip install numpy

RUN pip install matplotlib.pyplot

RUN pip install pandas

RUN apt -y update && apt -y install git

WORKDIR /mnt
