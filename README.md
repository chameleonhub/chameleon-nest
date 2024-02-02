# bahis-infra

BAHIS project infrastrucutre repository

## Docker

To install docker and other dependencies on a debian/ubuntu box:

```sh
sudo apt-get update

 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose postgresql-client

```

Or follow [this](https://docs.docker.com/engine/install/ubuntu/) tutorial.

## BAHIS

1. First you need to clone all the submodules

```sh
git submodule update --init --recursive
```

2. Then spin up the infrastructure you're interested in, e.g.

```sh
cd bahis-infra/serve/
sudo docker-compose build
sudo docker-compose up -d
```

3. To initialise the database for the first time request an initial db from one of the development team and run

```sh
cd pgdb
whichdb=<path-to-your-db>.sql ./resetdb.sh
```

4. Access BAHIS at e.g. [bahis-serve](http://localhost:83)
