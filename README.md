# OPC UA Database Pipeline
TODO add intro image with Docker, Compose, POSTGRESQL, OPC UA symbols, Redis symbols

## Description


## Flowchart
TODO add flowchart

## Prerequisites
- Prosys or other OPC UA signal generator
- Docker
- Docker Compose

## Usage
Run the following in cmd from the same folder as `docker-compose.yml` to build containers and start all processes in detached mode:
```
docker compose up -d
```

## TODO
- [ ] Prosys generator
- [ ] Python script subscribing to Prosys OPC UA nodes and sending to Redis queue
- [ ] Move Prosys-python script to Docker + requirements.txt
- [ ] Create Redis database
- [ ] Move Redis database to Docker
- [ ] Create barebones PostgreSQL database -> add commands to init.sql 
- [ ] Move Postgres to Docker
- [ ] Create Datasink from Redis to Postgres
- [ ] Add all images to `docker-compose.yml`
- [ ] Write main README description of all subprocesses + Docker/Docker compose
- [ ] Separate subprocesses to subrepos w/ individual READMEs
- [ ] Draw flowchart in drawio
- [ ] Add CI/CD Runner