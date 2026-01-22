FROM python:3.12.12-slim-bookworm

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY scripts/predict.py predict.py
COPY scripts/dtree_model.pkl dtree_model.pkl

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]