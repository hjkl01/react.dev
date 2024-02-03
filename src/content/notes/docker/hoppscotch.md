# API tool: httpbin hoppscotch

```yaml
version: "3.1"

services:
  httpbin:
    image: kennethreitz/httpbin
    container_name: httpbin
    restart: always
    ports:
      - "127.0.0.1:7999:80"

  hoppscotch:
    image: hoppscotch/hoppscotch:latest
    container_name: hoppscotch
    restart: always
    ports:
      - "127.0.0.1:3000:3000"

networks:
  default:
    external:
      name: nginx-proxy
```
