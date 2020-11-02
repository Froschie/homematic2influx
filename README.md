# homematic2influx
Scripts to transfer homematic data to Influx DB and Grafana Dashboards.

# Descriptions totally missing... to be added later



# compose2grafana.py
Helper script to query *docker-compose.yml* file and generate Grafana Datasource provisioning files.
`python3 compose2grafana.py [--ip 192.168.1.4] [--file docker-compose.yml]`

# homematic.py
Query XML API from Homematic CCU and transfer (nearly) all state informations to Influx DB.
```bash
mkdir homematic-query
cd homematic-query/
docker build --tag homematic-query .
docker-compose up -d
```

# homematic2grafana.py
Automatic generation of Grafana Dashboards based on Influx DB Homematic data.
`docker exec homematic-query python /homematic2grafana.py`
