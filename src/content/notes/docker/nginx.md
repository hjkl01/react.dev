# nginx-proxy-manager

```yaml
version: "3"
services:
  app:
    image: "jc21/nginx-proxy-manager:latest"
    restart: unless-stopped
    ports:
      - "80:80"
      - "81:81"
      - "443:443"
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

networks:
  default:
    external:
      name: nginx-proxy
```

```shell
# open http://127.0.0.1:81
# Default Admin User:
Email:    admin@example.com
Password: changeme
```
