# caddy

```shell
# 反向代理
news.hjkl01.cn {
    reverse_proxy 127.0.0.1:8000
    reverse_proxy api/* 127.0.0.1:8080

    encode zstd gzip

    header * {
        # cors
        Access-Control-Allow-Origin  *
        Access-Control-Allow-Methods "GET, POST, OPTIONS"
        header_upstream Host {host}
        header_upstream X-Real-IP {remote}
        header_upstream X-Forwarded-For {remote}
        header_upstream X-Forwarded-Proto {scheme}
    }
    # ssl
    # tls /etc/caddy/conf.d/example.com_nginx/example.com_bundle.pem /etc/caddy/conf.d/example.com_nginx/example.com.key

}


blog.hjkl01.cn {
    root * /data/blog
    templates
    file_server browse
    try_files {path} /index.html
    # try_files {path} {path}.html

    log {
        output file /var/log/caddy/access.log {
            roll_size 1gb
            roll_keep 5
            roll_keep_for 720h
        }
    }
}
```

### auth

```shell
caddy hash-password

basicauth /* {
        username output
}
```

### docker-compose.yml

```shell
version: "3.7"

services:
  caddy:
    image: caddy:alpine
    restart: unless-stopped
    container_name: caddy
    network_mode: "host"
    volumes:
      - ./data/caddy/Caddyfile:/etc/caddy/Caddyfile
      - ./data/caddy/cert:/data
```
