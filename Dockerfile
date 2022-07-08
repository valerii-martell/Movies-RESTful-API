FROM python:3.9

RUN useradd --create-home userapi
WORKDIR /movies_api

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
# CMD flask db stamp head
# CMD flask db migrate
# CMD flask db update
CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app