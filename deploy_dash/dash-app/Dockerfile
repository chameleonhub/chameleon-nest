FROM python:3.10

RUN pip install pipenv

ENV PROJECT_DIR=/bahis-dash

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy

CMD ["uwsgi", "wsgi.ini"]
