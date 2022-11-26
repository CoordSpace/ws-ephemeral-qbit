FROM python:3.11-slim as base

from base as builder

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install wheel && pip3 wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /tmp/requirements.txt

FROM base

ENV WS_USERNAME=${WS_USERNAME}
ENV WS_PASSWORD=${WS_PASSWORD}
ENV QB_USERNAME=${QB_USERNAME}
ENV QB_PASSWORD=${QB_PASSWORD}
ENV QB_EPHEMERAL_PORT=${QB_PORT}

WORKDIR /app

COPY --from=base /wheels /wheels

RUN pip3 install --no-cache-dir /wheels/*

COPY src/ .

CMD ["python3", "run.py"]