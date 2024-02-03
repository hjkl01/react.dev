# movies

## aria2

```yaml
version: "3.8"

services:
  Aria2-Pro:
    container_name: aria2-pro
    image: p3terx/aria2-pro
    environment:
      - PUID=65534
      - PGID=65534
      - UMASK_SET=022
      - RPC_SECRET=updateme!!!
      - RPC_PORT=6800
      - LISTEN_PORT=6888
      - DISK_CACHE=64M
      - IPV6_MODE=true
      - UPDATE_TRACKERS=true
      - CUSTOM_TRACKER_URL=
      - TZ=Asia/Shanghai
    volumes:
      - ${PWD}/data/aria2-config:/config
      - ${PWD}/data/downloads:/downloads
    network_mode: host
    # network_mode: bridge
    # ports:
    #   - 6800:6800
    #   - 6888:6888
    #   - 6888:6888/udp
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 1m

  AriaNg:
    container_name: ariang
    image: p3terx/ariang
    command: --port 6880 --ipv6
    # network_mode: host
    ports:
      - 127.0.0.1:6880:6880
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 1m

  # jellyfin
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin_server
    volumes:
      - ./data/jellyfin/config:/config # Configuration directory
      - ./data/jellyfin/cache:/cache
      - ./data/downloads:/downloads
    ports:
      - 127.0.0.1:8096:8096
    restart: unless-stopped

  alist:
    container_name: alist
    image: xhofe/alist:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:5244:5244"
    volumes:
      - ./data/alist:/opt/alist/data
      - ./data/downloads:/mnt

networks:
  default:
    external:
      name: nginx-proxy
```

## caddy

```shell
movies.domain.com {
    reverse_proxy 127.0.0.1:8096
    encode zstd gzip
}

aria.domain.com {
    reverse_proxy 127.0.0.1:6800
    encode zstd gzip
}
```

## nginx

[链接](/notes/linux/nginx)

<!-- ## emby -->
<!-- ```yaml -->
<!-- version: "2.3" -->
<!-- services: -->
<!--   emby: -->
<!--     image: emby/embyserver -->
<!--     container_name: embyserver -->
<!--     runtime: nvidia # Expose NVIDIA GPUs -->
<!--     # network_mode: host # Enable DLNA and Wake-on-Lan -->
<!--     environment: -->
<!--       - UID=1000 # The UID to run emby as (default: 2) -->
<!--       - GID=100 # The GID to run emby as (default 2) -->
<!--       - GIDLIST=100 # A comma-separated list of additional GIDs to run emby as (default: 2) -->
<!--     volumes: -->
<!--       - ./data/embyserver/programdata:/config # Configuration directory -->
<!--       - ./data/embyserver/tvshows:/mnt/share1 # Media directory -->
<!--       - ./data/embyserver/movies:/media -->
<!--     ports: -->
<!--       - 8096:8096 # HTTP port -->
<!--       # - 8920:8920 # HTTPS port -->
<!--     devices: -->
<!--       - /dev/dri:/dev/dri # VAAPI/NVDEC/NVENC render nodes -->
<!--     #   - /dev/vchiq:/dev/vchiq # MMAL/OMX on Raspberry Pi -->
<!--     restart: unless-stopped       -->
<!-- ``` -->
