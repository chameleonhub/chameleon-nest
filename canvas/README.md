# How to deploy the BAHIS dashboard

1. Clone the infrastructure repository with `git clone git@github.com:chameleon/chameleon-nest.git` or `git repo clone chameleon/chameleon-nest`
2. Clone the submodules (`chameleon-dash` and `chameleon-data`) with `git submodule update --init --recursive` (`cd` into the repo first)
3. Make sure that `bahis_creds_file.cnf` is in `chameleon-data` directory.
4. Make sure the `output` directory in `chameleon-data` is full (or run the script in the container to fill it).
5. Make sure `secret-init_user.sql` is in `pgdb` directory to create a user for bahis data to connect to our dashboard/backup database. It is just a one-liner `CREATE USER kobo WITH PASSWORD 'XXXXXXXXX';`
6. Make sure backups of the production databsed are written to `chameleon-data/input`
7. Make sure to put in `chameleon-data/input` our side-loaded files from oldbahis and corrected disease list: `Diseaselist.csv`, `oldbahis_fao_species[timestamp].csv`, `oldbahis_forms_data[timestamp].csv`
8. `docker-compose up -d`

## To update a module (e.g. chameleon-dash or chameleon-data)

1. `docker compose down -v` - this stops the current deployment, takes the containers down _and_ should take volumes down too (not always needed but probably good pratice)
2. `git submodule update --recursive` - this updates all submodules to the latest commit on their current branch (use `git submodule foreach "git branch --show-current"` to see submodule branches)
3. `docker-compose up -d` - this starts the deployment again

## How it works

`chameleon-data` has a cron script that runs a pandas pipeline that resets datbase from backup and pulls most recent data to csv files (including bahistot/oldbahis that are manually put in `input` directory). Those files written to `output` are then mounted to chameleon-dash directory `exported_data` by docker-compose.

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
