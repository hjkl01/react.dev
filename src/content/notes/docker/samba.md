# samba nfs

## samba

```yaml
version: "3.4"

services:
  samba:
    image: dperson/samba
    environment:
      TZ: "EST5EDT"
    ports:
      - "139:139/tcp"
      - "445:445/tcp"
    read_only: false
    restart: unless-stopped
    volumes:
      - ./data:/mnt:z
      - ./data:/mnt:ro
    command: '-s "Volume;/mnt;yes;no;no;foo" -u "foo;bar" -p'
           # "<name;/path>[;browse;readonly;guest;users;admins;writelist;comment]"

networks:
  default:
    external:
      name: nginx-proxy
```

## nfs

```yaml
version: "2.1"
services:
  # https://hub.docker.com/r/itsthenetwork/nfs-server-alpine
  nfs:
    image: itsthenetwork/nfs-server-alpine:12
    container_name: nfs
    restart: unless-stopped
    privileged: true
    environment:
      - SHARED_DIRECTORY=/data
    volumes:
      - ./data/jellyfin/movies:/data
    ports:
      - 2049:2049

networks:
  default:
    external:
      name: nginx-proxy
```
