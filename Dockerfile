FROM python:3.12-slim-bookworm

RUN pip install pipenv --no-cache-dir pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy --ignore-pipfile

COPY scripts/predict.py predict.py
COPY scripts/dtree_model.pkl dtree_model.pkl
COPY scripts/predict-test.py test.py

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]