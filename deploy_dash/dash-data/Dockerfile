#FROM python:3.10
FROM ubuntu:22.04

RUN apt update
RUN apt install -y postgresql-client python3-pip cron

RUN pip install pipenv

ENV PROJECT_DIR=/bahis-data/server-scripts

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy

# Add crontab entry. The following schedules the script to run daily at midnight.
RUN (echo "0 23 * * * cd /bahis-data/server-scripts/ && sh nightly.sh >> log.txt") | crontab -

# Start cron in the foreground (this is often added as the CMD or ENTRYPOINT for the container if you're using cron)
CMD ["cron", "-f"]
