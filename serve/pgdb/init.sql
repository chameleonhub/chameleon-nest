\set ON_ERROR_STOP on
drop database if exists coredb;
drop user if exists kobo;
CREATE USER kobo WITH PASSWORD 'bahis@321';
create database coredb;
GRANT ALL PRIVILEGES ON DATABASE coredb to kobo;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
