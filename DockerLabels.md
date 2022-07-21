# Docker Labels (Opencontainer Annotations)

Docker nennt [Opencontainer Annotationen](https://github.com/opencontainers/image-spec/blob/main/annotations.md) Labels. Labels sind Metadaten im Key-Value format.

Vordefinierte annotations keys enthalten Titel, Author und Version eines Images.

## Image Annotationen
Annotationen müssen vom Author gepflegt werden

```Dockerfile
LABEL org.opencontainers.image.title "MeinContainer"
```

```shell
docker inspect $(docker image ls -aqq) --format='{{ .Id }} {{ index .Config.Labels "org.opencontainers.image.title" }}'
```

## Container Annotationen
Laufzeitannotationen, die beim starten des containers hinzugefügt werden können.

In docker-compose kann das etwa so aussehen:

```yaml
version: "3.2"

services:  
  whoami:
    image: traefik/whoami
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.whoami.rule=Host(`whoami.localhost`)"
      - "traefik.http.routers.whoami.entrypoints=web"
```

```shell
docker inspect $(docker ps -aq) --format='{{ .Id }} {{ index .Config.Labels "traefik.http.routers.whoami.rule"  }}'
```