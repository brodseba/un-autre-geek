FROM python:3.8-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV EXPLAIN_TEMPLATE_LOADING=True
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 runApi:app