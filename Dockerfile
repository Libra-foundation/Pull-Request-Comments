FROM python:3.10.9-slim

COPY entrypoint.py /entrypoint.py
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENTRYPOINT python /entrypoint.py