# prest

```yaml
# https://github.com/prest/prest#test-using-docker
version: "3"
services:
  postgres:
    image: postgres
    volumes:
      - "./data/postgres:/var/lib/postgresql/data"
    environment:
      - POSTGRES_USER=prest
      - POSTGRES_DB=prest
      - POSTGRES_PASSWORD=prest
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready", "-U", "prest"]
      interval: 30s
      retries: 3
  prest:
    # use latest build - analyze the risk of using this version in production
    image: prest/prest
    links:
      - "postgres:postgres"
    environment:
      - PREST_DEBUG=false
      - PREST_AUTH_ENABLED=true
      - PREST_PG_HOST=postgres
      - PREST_PG_USER=prest
      - PREST_PG_PASS=prest
      - PREST_PG_DATABASE=prest
      - PREST_PG_PORT=5432
      - PREST_SSL_MODE=disable
    depends_on:
      postgres:
        condition: service_healthy
    ports:
      - "3000:3000"

networks:
  default:
    external:
      name: nginx-proxy
```
