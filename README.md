# bahis-infra

BAHIS project infrastrucutre repository

## Docker

To install docker and other dependencies on a debian/ubuntu box:

```basg
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

## BAHIS3

From the root of this repository.

### UP

```bash
docker-compose -f kobo-docker/docker-compose.backend.primary.yml -f kobo-docker/docker-compose.backend.primary.override.yml up -d && docker-compose -f kobo-docker/docker-compose.frontend.yml -f docker-compose.frontend.dev.yml up -d
```

### DOWN

```bash
docker-compose -f kobo-docker/docker-compose.backend.primary.yml -f kobo-docker/docker-compose.backend.primary.override.yml down && docker-compose -f kobo-docker/docker-compose.frontend.yml -f docker-compose.frontend.dev.yml down
```

### Mega purge of local machine

This is like the big red button - so only use it locally and never on the server.

```bash
docker system prune --volumes --all --force
docker volume prune --force --filter all=1

````
