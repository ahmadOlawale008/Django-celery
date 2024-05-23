FROM python:3.12.3-alpine3.19
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

RUN echo "Website Open to view"