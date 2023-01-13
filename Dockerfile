FROM python:3.9.16-slim-bullseye

EXPOSE 80

WORKDIR /model-serve

COPY ./requirements.txt /model-serve/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /model-serve/requirements.txt

COPY ./app /model-serve/app

COPY ./models /model-serve/models

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
