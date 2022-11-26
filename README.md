# setup
```
docker-compose up -d --build
```
# fastapi
http://localhost:8000/docs

# mysql 접속
```
docker ps

docker exec -it [db_name] /bin/bash

mysql -p

mysql -uroot -p[password]

USE test_db;

alter table userinfo drop primary key,change id id INT NOT NULL;

SELECT * FROM userinfo;

ALTER TABLE userinfo ADD UID int PRIMARY KEY AUTO_INCREMENT;

DESC userinfo;
```
