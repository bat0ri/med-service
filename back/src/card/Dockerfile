FROM python:3.11.2-alpine

EXPOSE 8001

WORKDIR .

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry


RUN pip install uvicorn

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi



