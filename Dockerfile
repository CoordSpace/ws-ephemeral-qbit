FROM python:3.10-alpine as base

from base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python3 -m pip install -U pip
RUN python -m pip install --install-option="--prefix=/install"  -r requirements.txt

FROM base

ENV WS_USERNAME=${WS_USERNAME}
ENV WS_PASSWORD=${WS_PASSWORD}
ENV QB_USERNAME=${QB_USERNAME}
ENV QB_PASSWORD=${QB_PASSWORD}
ENV QB_EPHEMERAL_PORT=${QB_PORT}

COPY --from=builder /install /usr/local
COPY src /app
WORKDIR /app

CMD ["python3", "run.py"]