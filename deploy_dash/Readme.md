# Deployment of bahis dash

1. Clone repositories:
```
git@github.com:road86/bahis-infra.git
git@github.com:road86/bahis-data.git
git@github.com:road86/bahis-dash.git
```
2. Make sure that `bahis_creds_file.cnf` is in `bahis-data` directory.
3. Make sure `secret-init_user.sql` is in `dash-db` directory to create a user for bahis data to connect to our dashboard/backup database
3. Make sure backups of the production databsed are written to `/home/bahis/backups` 
4. Make sure to put in `bahis-data/input` our side-loaded files from oldbahis and corrected disease list:
```
Diseaselist.csv
oldbahis_fao_species[timestamp].csv
oldbahis_forms_data[timestamp].csv
```

5. `docker-compose up`

# How it works
`bahis-data` has a cron script that runs a pandas pipeline that resets datbase from backup and pulls most recent data to csv files (including bahistot/oldbahis that are manually put in `input` directory`. Those files written to output are then copied to bahis-dash directory `exported_data` where they are used for display
