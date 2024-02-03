# code server

## docker-compose.yml

- [address](https://github.com/linuxserver/docker-code-server)

```yaml
---
version: "2.1"
services:
  code-server:
    image: lscr.io/linuxserver/code-server:latest
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - PASSWORD=secrets #optional
      - HASHED_PASSWORD= #optional
      - SUDO_PASSWORD=secrets #optional
      - SUDO_PASSWORD_HASH= #optional
      - PROXY_DOMAIN=code-server.my.domain #optional
      - DEFAULT_WORKSPACE=/somedir #optional
    volumes:
      - ./data/code_server/config:/config
      - /home/user/somedir:/somedir
    ports:
      - 192.168.32.4:8443:8443
    restart: unless-stopped

networks:
  default:
    external:
      name: nginx-proxy
```
