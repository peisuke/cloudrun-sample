FROM python:3.6

ADD run.py /

RUN pip install flask gunicorn
ENV PORT=8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 run:app
