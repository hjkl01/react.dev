# music

## [mStream](https://github.com/IrosTheBeggar/mStream)

```yaml
---
version: "2.1"
services:
  mstream:
    image: lscr.io/linuxserver/mstream:latest
    container_name: mstream
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
    volumes:
      - ./data/mstream/config:/config
      - ./data/mstream/music:/music
    ports:
      - 127.0.0.1:3000:3000
    restart: unless-stopped

networks:
  default:
    external:
      name: nginx-proxy
```

## Navidrome

```yaml
version: "3"
services:
  navidrome:
    container_name: navidrome
    image: deluan/navidrome:latest
    user: 0:0 #0:0代表用root用户运行
    ports:
      - "127.0.0.1:4533:4533"
    restart: unless-stopped
    environment:
      # Optional: put your config options customization here. Examples:
      ND_SCANSCHEDULE: 1h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
      ND_ENABLETRANSCODINGCONFIG: "true"
      ND_TRANSCODINGCACHESIZE: "4000M"
      ND_IMAGECACHESIZE: "1000M"
    volumes:
      - "./data/navidrome/data:/data"
      - "./data/mstream/music:/music"

networks:
  default:
    external:
      name: nginx-proxy
```
