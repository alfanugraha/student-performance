FROM python:3.12.7-slim-bookworm

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY scripts/predict.py predict.py
COPY scripts/dtree_model.pkl dtree_model.pkl
COPY scripts/predict-test.py test.py

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]