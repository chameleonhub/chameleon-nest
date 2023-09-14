# How to deploy the BAHIS dashboard

1. Clone the infrastructure repository with `git clone git@github.com:road86/bahis-infra.git` or `git repo clone road86/bahis-infra`
2. Clone the submodules (`bahis-dash` and `bahis-data`) with `git submodule update --init --recursive`
3. Make sure the `output` directory in `bahis-data` is full (or run the script in the container to fill it).
4. Make sure that `bahis_creds_file.cnf` is in `bahis-data` directory.
5. Make sure `secret-init_user.sql` is in `pgdb` directory to create a user for bahis data to connect to our dashboard/backup database. It is just a one-liner `CREATE USER kobo WITH PASSWORD 'XXXXXXXXX';`
6. Make sure backups of the production databsed are written to `/home/bahis/backups`
7. Make sure to put in `bahis-data/input` our side-loaded files from oldbahis and corrected disease list: `Diseaselist.csv`, `oldbahis_fao_species[timestamp].csv`, `oldbahis_forms_data[timestamp].csv`
8. `docker-compose up -d`

## How it works

`bahis-data` has a cron script that runs a pandas pipeline that resets datbase from backup and pulls most recent data to csv files (including bahistot/oldbahis that are manually put in `input` directory). Those files written to `output` are then mounted to bahis-dash directory `exported_data` by docker-compose.

## bahis_creds_file.cnf

This file is used by sqlalchemy to access database with BAHIS backup and looks like this:

```toml
[bahis_credentials]
database=coredb
user=kobo
port=5432
password=XXXXXXXXX
host=pgdb
```
