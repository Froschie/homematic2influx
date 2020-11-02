# homematic2influx
Scripts to transfer homematic data to Influx DB and Grafana Dashboards.

-----
-----
# Descriptions and script development still ongoing...
-----
-----

# compose2grafana.py
Helper script to query *docker-compose.yml* file and generate Grafana Datasource provisioning files.
`python3 compose2grafana.py [--ip 192.168.1.4] [--file docker-compose.yml]`

Example output:
```
2020-11-02 13:00:00.000000 File "influxdb_homematic.yaml" written.
```

Example *influxdb_homematic.yaml* file:
```yaml
apiVersion: 1
datasources:
- access: proxy
  basicAuth: false
  database: homematic
  editable: true
  isDefault: false
  name: influxdb_homematic
  orgId: 1
  secureJsonData:
    password: userpw
  type: influxdb
  url: http://192.168.1.3:8086
  user: user
  version: 1
```


## Create Docker Container
```bash
mkdir homematic-query
cd homematic-query/
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/Dockerfile
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/homematic.py
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/homematic2grafana.py
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/homematic2grafana_templates.py
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/homematic2grafana_list.py
docker build --tag homematic-query .
```


## Start Docker Container via Docker-Compose File
```bash
curl -O https://raw.githubusercontent.com/Froschie/homematic2influx/main/docker-compose.yml
vi docker-compose.yml
mkdir /influxdb-homematic-db
mkdir -p /grafana/dashboards
mkdir -p /grafana-provisioning/dashboards
docker-compose up -d
```
*Note: please adapt the parameters as needed! Don´t override your existing docker compose file!*


# homematic.py
Query XML API from Homematic CCU and transfer (nearly) all state informations to Influx DB.  
This script will run automatically after starting the docker container.

Example docker container logs:
```
2020-11-02 12:00:00.010000 Querying Homematic Data...
2020-11-02 12:00:01.150000 InfluxDB write data successfull: 500
2020-11-02 12:00:01.160000 Cycle completed in: 0:00:01.160000
2020-11-02 12:01:00.010000 Querying Homematic Data...
2020-11-02 12:01:01.150000 InfluxDB write data successfull: 500
2020-11-02 12:01:01.160000 Cycle completed in: 0:00:01.160000
```


# homematic2grafana.py
Automatic generation of Grafana Dashboards based on Influx DB Homematic data.  
`docker exec homematic-query python /homematic2grafana.py`

Example output:
```
2020-11-02 12:00:00.000000 File "ACTUAL_HUMIDITY.json" written.
```

In oder to use the generated dashboards, first loading of provisioned dashboards need to be enabled.  
*homematic_dashboard.yaml* file needs to be mapped to */etc/grafana/provisioning* directory in Grafana Container.  
Based on the example *docker-compose.yml* file, copy the *homematic_dashboard.yaml* file to */grafana-provisioning/dashboards/homematic_dashboard.yaml*:  
`curl https://raw.githubusercontent.com/Froschie/homematic2influx/main/homematic_dashboard.yaml -o /grafana-provisioning/dashboards/homematic_dashboard.yaml`


# homematic2grafana_list.py
Lists the amount of measurements stored in the Influx DB database.  
`docker exec homematic-query python /homematic2grafana_list.py [--fields] [--devices]`

Example output:
```
Measurements:
  ACTUAL_HUMIDITY, Points: 1008
    ACTUAL_HUMIDITY_2 (Field), Points: 1008
      Room 123 (Device), Points: 1008
Summary:
  Measurements: 1006
```
