# netdata

```yaml
version: "3"
services:
  netdata:
    image: netdata/netdata
    container_name: netdata
    hostname: 192.168.32.5
    ports:
      - 19999:19999
    restart: unless-stopped
    cap_add:
      - SYS_PTRACE
    security_opt:
      - apparmor:unconfined
    volumes:
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro

networks:
  default:
    external:
      name: nginx-proxy
```
