# mongoDB

```shell
# .env
MONGO_ROOT_USER=username
MONGO_ROOT_PASSWORD=password
MONGODB_URL=mongodb://username:password@mongo:27017
```

```yaml
version: "3.1"

services:
  mongo:
    image: mongo
    restart: always
    ports:
      - 27017:27017
    environment:
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_ROOT_USER}
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_ROOT_PASSWORD}
    volumes:
      - ./data/mongo:/data/db

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    links:
      - mongo
    environment:
      - ME_CONFIG_MONGODB_URL=${MONGODB_URL}
      - ME_CONFIG_BASICAUTH_USERNAME=${MONGO_ROOT_USER}
      - ME_CONFIG_BASICAUTH_PASSWORD=${MONGO_ROOT_PASSWORD}

networks:
  default:
    external:
      name: nginx-proxy
```

## export && restore

```
yay --noconfirm -S mongodb-tools-bin

USER=''
PASSWD=''
HOST='192.168.32.6'
PORT='27017'

echo $(date +%s)
echo $(date +%c)
echo $(date +%Y%m%d_%H%M%S)
FILENAME=sql/${HOST}_$(date +%Y%m%d_%H%M%S).json

mongodump --uri=mongodb://${USER}:${PASSWD}@${HOST}:${PORT}/ --authenticationDatabase=admin -o ${FILENAME}
# mongorestore --uri=mongodb://${USER}:${PASSWD}@${HOST}:${PORT}/ --authenticationDatabase=admin --dir ${FILENAME}
```
