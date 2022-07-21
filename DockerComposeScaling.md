# Scaling

Scaling kann in `docker-compose.yaml` festgelegt werden oder per CLI angepasst werden

## `docker-compose.yaml`
```yaml
version: "3.2"

services:  
  whoami:
    image: traefik/whoami
    scale: 2
```

## CLI
```shell
docker-compose scale whoami=10
```