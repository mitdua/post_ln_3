FROM python:3.12.4

WORKDIR /core
COPY requirements.txt /core/
RUN pip install --no-cache-dir -r requirements.txt
COPY /core/ /core/