FROM python:3.8-alpine
#RUN find / -perm +6000 -type f -exec chmod a-s {} \; || true
RUN apk update && apk add --no-cache build-base linux-headers
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 runApi:app