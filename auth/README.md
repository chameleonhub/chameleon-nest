# How to deploy
1. Clone bahis-infra repo with git clone
```bash
git clone https://github.com/road86/bahis-infra
```
2. Update submodule with 
3. ```bash
   cd bahis-infra
   git submodule update --init --recursive
   ```
3. Run the docker compose

```bash
cd bahis-infra/auth/
sudo docker-compose build
sudo docker-compose up -d
```

