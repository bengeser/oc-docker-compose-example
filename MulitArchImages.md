# Multi Architecture images

[Ungetestet, basierend auf diesem Artikel](https://www.docker.com/blog/multi-platform-docker-builds/)

Docker ist nur eine dünne abstraktiosschicht über dem Linux betriebssystemkernel.
Daher ist es nötig, dass die Programme innerhalb des containers auf der Prozessorarchitektur des Hostsystems laufen.

Damit Docker(-Compose)files oder ähnliche Systeme nicht pro Architektur gepflegt werden müssen, wird das innerhalb von Docker geregelt:

``` shell
docker manifest inspect [IMAGE]
```

## Bauen images mit buildx (Cross-Compilation)
 Welche Architekturen werden für Cross-Compilation unterstützt?
```shell
$ docker buildx ls

NAME/NODE     DRIVER/ENDPOINT STATUS                 PLATFORMS
desktop-linux                 protocol not available 
default *     docker                                 
  default     default         running                linux/amd64, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
```


