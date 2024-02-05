psql -U postgres -h localhost -p 99 -f init.sql
psql -U postgres -d coredb  -h localhost -p 99 --set ON_ERROR_STOP -f tmp.sql
pg_dump -U postgres -d coredb  -h localhost -p 99 > tmp.sql
