FROM python:3.7

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir metapy pytoml scrapy

WORKDIR /home/python/app

# infinite loop
ENTRYPOINT ["tail", "-f", "/dev/null"]

# CMD ["python", "myspider.py"]