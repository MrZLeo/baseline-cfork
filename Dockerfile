FROM ddnirvana/python-base-image:dev-base-3.6

RUN pip3 install flask waitress

COPY daemon.py /

CMD ["python3", "daemon.py"]
