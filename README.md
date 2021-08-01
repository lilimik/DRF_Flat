## Terminal 1
docker-compose up

---

docker-compose up -d


## Terminal 2
```sh
docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                                       NAMES
0fb320ea3aaa   postgres:11.1-alpine   "docker-entrypoint.s…"   55 seconds ago   Up 54 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   drf_flat_database_1
```

```sh
docker exec -it drf_flat_database_1 bash
bash-4.4# psql -U postgres
psql (11.1)
Type "help" for help.

postgres=# ALTER USER postgres PASSWORD 'flat';
ALTER ROLE
```
