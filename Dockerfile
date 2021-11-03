FROM python:3

ADD ping-exporter/ping-exporter.py /

RUN pip install ping3 prometheus_client

CMD ["python", "./ping-exporter.py"]
