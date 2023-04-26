FROM python:3.10-alpine3.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN pip install --upgrade pip

WORKDIR /app
RUN mkdir static

COPY . /app
COPY /transfiguration_data/static/ /app/static/

ENV STATIC_URL /static/
ENV STATIC_ROOT /app/static

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput"]
