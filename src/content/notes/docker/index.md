---
sidebar_position: 0
---

# docker

## install

```shell
wget -qO- https://get.docker.com/ | sh
sudo usermod -aG docker $USER

# 修改源 /etc/docker/daemon.json
{
    "registry-mirrors": [
        "http://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "https://dockerproxy.com",
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://f1361db2.m.daocloud.io",
        "https://dockerhub.azk8s.cn"
    ]
}
```

## 常用命令

```shell
# export
docker save -o <path for generated tar file> <image name>
example: docker save -o ./centos.tar centos:16

# load
docker load -i <path to image tar file>

# run image
docker run -it ubuntu bash

# exec container
docker exec -it openwrt zsh
```

## tools

- ctop
- lazydocker

```shell
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/.config/jesseduffield/lazydocker lazyteam/lazydocker
```

- portainer

```shell
version: '3.1'

services:

  portainer:
    image: portainer/portainer
    restart: always
    ports:
      - 8000:8000
      - 9000:9000
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./data/portainer:/data

networks:
  default:
    external:
      name: nginx-proxy

# docker network create nginx-proxy
```

## [减少镜像体积](https://icloudnative.io/posts/docker-images-part1-reducing-image-size/)

```go
// hello.go
package main

import "fmt"

func main () {
  fmt.Println("Hello, world!")
}
```

```shell
# Dockerfile
FROM golang
COPY hello.go .
RUN go build hello.go
# FROM scratch
# FROM alpine
FROM busybox:glibc
COPY --from=0 /go/hello .
CMD ["./hello"]
```
