FROM python:3.8-alpine
RUN find / -perm +6000 -type f -exec chmod a-s {} \; || true
RUN groupadd -r geek && useradd -r -s /bin/false -g geek geek
RUN apk update && apk add --no-cache build-base linux-headers
WORKDIR /app
COPY . .
RUN chown -R geek:geek /app
USER geek
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 runApi:app