FROM python:3.8.5-buster

WORKDIR /usr/src/app
COPY examples/react_flask ./
COPY structure ./structure
COPY install-nginx.sh ./
RUN bash install-nginx.sh
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--socket","0.0.0.0:5000","--protocol=http","-w","wsgi:app"]
