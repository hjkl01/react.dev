# mysql

## docker-compose.yml

```yaml
version: "3.1"

services:
  db:
    # We use a mariadb image which supports both amd64 & arm64 architecture
    image: mariadb:10.6.4-focal
    # If you really want to use MySQL, uncomment the following line
    #image: mysql:8.0.27
    command: "--default-authentication-plugin=mysql_native_password"
    volumes:
      - ./data/mysql:/var/lib/mysql
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=data
      - MYSQL_USER=user
      - MYSQL_PASSWORD=password
      - MYSQL_ROOT_HOST=%
    ports:
      - 3306:3306

networks:
  default:
    external:
      name: nginx-proxy
```

### linux 配置

```shell
/etc/mysql/my.cnf:

[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
```

### others

```shell
protected-mode yes

mysqldump -u root -p --all-databases > data.txt
source data.txt

CREATE DATABASE testDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pwiz-a-model-generator
```
