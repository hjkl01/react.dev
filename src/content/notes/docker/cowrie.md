# cowrie

## Cowrie SSH/Telnet Honeypot

## https://github.com/cowrie/cowrie

## docker-compose.yml

```yaml
version: "3"

services:
  cowrie:
    image: cowrie/cowrie:latest
    container_name: cowrie
    restart: always
    ports:
      - 22:2222

networks:
  default:
    external:
      name: nginx-proxy
```
