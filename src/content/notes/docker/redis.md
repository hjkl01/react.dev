# redis

## redis 及其持久化

### redis.conf

```shell
requirepass 123456
appendonly yes
daemonize no
```

## docker-compose.yml

```yaml
version: "3"
services:
  redis:
    image: redis
    restart: unless-stopped
    # command: redis-server --requirepass 123456
    command: redis-server /usr/local/etc/redis/redis.conf
    ports:
      - 6379:6379
    volumes:
      - ./redis.conf:/usr/local/etc/redis/redis.conf
      - ./data/redis:/data/

networks:
  default:
    external:
      name: nginx-proxy
```
