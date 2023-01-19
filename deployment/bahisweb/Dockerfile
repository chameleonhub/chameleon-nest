#base image
FROM ubuntu:20.04

#Env variables which are needed for build need to be in this file or passed as command line arguments. Sadly....
ENV DEBIAN_FRONTEND=noninteractive
ENV BAHIS_ENV=/opt/envbahis
ENV PATH="$BAHIS_ENV/bin:$PATH"
ENV DJANGO_SETTINGS_MODULE="kobocat_settings"
ENV SRC_DIR="/src_bahis"
ENV PYTHONPATH="$SRC_DIR/env:$PYTHON_PATH"
ENV V_R="/"
ENV V_E="$SRC_DIR"
ENV ip="0.0.0.0"
ENV KOBOCAT_PATH="$SRC_DIR/kobocat"
ENV KOBOCAT_TEMPLATES_PATH="$SRC_DIR/kobocat-template"

#Datbase Information most of those will need to go to docker-compose
ENV PSQL_ADMIN="postgres"
ENV KOBO_PSQL_DB_NAME="coredb"
ENV KOBO_PSQL_DB_USER="kobo"
ENV KOBO_PSQL_DB_PASS="bahis@321"
ENV KOBO_PSQL_DB_HOST="pgdb"
ENV DATABASE_URL="postgis://$KOBO_PSQL_DB_USER:$KOBO_PSQL_DB_PASS@$DATABASE_SERVER_IP:5432/$KOBO_PSQL_DB_NAME"

#settings specific details
ENV DJANGO_LIVE_RELOAD="False"
ENV DJANGO_SITE_ID="1"
ENV DJANGO_SECRET_KEY="P2Nerc3oG2564z5mHTGUhAoh2CzOMVenWBNMNWgWU796n"
ENV CLEAN_APT_CACHE="True"

#db settings
ENV MONGO_DB_NAME="coredb"
ENV MONGO_DB_USER=""
ENV MONGO_DB_PASSWORD="PASSWORD"
ENV MONGO_DB_HOST="mongodb"

RUN apt update

RUN apt -y install net-tools python-dev gfortran libatlas-base-dev libjpeg-dev python-numpy   python-pandas-doc openjdk-8-jre zlib1g-dev binutils libproj-dev libxslt1-dev libxslt1-dev libxml2-dev libmemcached-dev python-lxml  virtualenv nodejs  uuid-dev libcap-dev libpq-dev   python-dev build-essential uwsgi  unzip  wget ca-certificates git postgresql-client binutils libproj-dev gdal-bin

RUN virtualenv -p /usr/bin/python2.7 $BAHIS_ENV

RUN apt -y update
#    https://stackoverflow.com/questions/53904157/numpy-ufunc-has-the-wrong-size-try-recompiling-even-with-the-latest-pandas-and#54010510
# must be installed separately first, it isn't enough to have it earlier in requirements file
RUN pip install numpy==1.15.2
COPY requirements.txt .
RUN pip install -r requirements.txt

#Patching libgeos
COPY libgeos.py_fix .
RUN mv libgeos.py_fix $BAHIS_ENV/lib/python2.7/site-packages/django/contrib/gis/geos/libgeos.py

#Don't ask... uwsgi with python2 plugin, what a disaster
RUN wget https://github.com/unbit/uwsgi/archive/refs/tags/2.0.20.tar.gz
RUN tar xf 2.0.20.tar.gz
RUN cd uwsgi-2.0.20 && make PROFILE=nolang && PYTHON=python2.7 ./uwsgi --build-plugin "plugins/python python27"

#ADD https://api.github.com/repos/road86/bahis-serve/git/refs/heads/main version.json
#RUN git clone https://github.com/road86/bahis-serve.git $SRC_DIR

#use the following to edit code locally
# RUN mkdir $SRC_DIR
# COPY src $SRC_DIR
WORKDIR /uwsgi-2.0.20

COPY bahis.ini .

COPY celeryd_bahis .
RUN chmod +x celeryd_bahis
RUN export > all_env_vars.sh

ENV KOBO_SERVER_HOST="localhost"
ENV KOBO_RENDERER_HOST="localhost/form-renderer"
ENV DJANGO_DEBUG="False"

#CMD ["./uwsgi", "bahis.ini"]
#we need 10s delay to give databases time to initialise
CMD sleep 10 && python /${SRC_DIR}/kobocat/manage.py collectstatic --noinput && ./celeryd_bahis start && ./uwsgi bahis.ini
