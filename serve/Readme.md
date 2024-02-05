

```
sudo docker_compose build
sudo docker_compose up -d
```

To initialise database for the first time: 
```
psql -U postgres -h localhost -p 99 < pgdb/init.sql
psql -U postgres -h -d coredb localhost -p 99 < pgdb/bahis_minimal.sql
```
you need to download bahis minimal separately
