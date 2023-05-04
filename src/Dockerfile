FROM python:3.10.8-bullseye

ENV \
    PYTHONPATH=/usr/local/bin/python3 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir -p /src
COPY ./ /src
# COPY ./requirements.txt /src
RUN \
    pip install --upgrade wheel \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r /src/requirements.txt

WORKDIR /src

EXPOSE 8000

CMD \
    # && gunicorn main:app -w 2 -b 0.0.0.0:8000\
    python start_bot.py
