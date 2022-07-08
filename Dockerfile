FROM python:3.10-alpine

EXPOSE 8001
WORKDIR /
COPY ./requirements.txt /requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/src"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Jerusalem

RUN set -xe
RUN apk add --update --no-cache --virtual .build-deps curl postgresql-libs gcc musl-dev postgresql-dev tini
RUN pip install -r /requirements.txt
RUN rm -rf /var/cache/apk/* /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache /requirements.txt

COPY ./src /src

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]