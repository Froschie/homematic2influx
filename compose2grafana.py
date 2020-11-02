# -*- coding: utf-8 -*-
import sys
if not sys.version_info >= (3, 5):
    print("Python version is " + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + ". Please start with python version >=3.5!")
    sys.exit(1)

from datetime import datetime
import os
import argparse
from pathlib import Path
import yaml

parser=argparse.ArgumentParser(
    description='''Script for generating Grafana Datasource config files out of docker compose yaml file.''')
parser.add_argument('-f', '--file', type=str, required=False, default="docker-compose.yml", help='Docker Compose input file.')
parser.add_argument('-i', '--ip', type=str, required=False, default="192.168.1.3", help='IP of Influx DB Server.')
args=parser.parse_args()

try:
    f = open(args.file, "r")
    compose_yaml = yaml.load_all(f.read(), Loader=yaml.FullLoader)
    f.close()
except:
    print(datetime.now(), "File \"" + args.file + "\" could not be opened!" )
    sys.exit(1)

def yaml_template(name, ip, port, user, pw, db):
    return { 'apiVersion': 1,
             'datasources': [
                {  'name': name,
                   'type': 'influxdb',
                   'access': 'proxy',
                   'orgId': 1,
                   'url': 'http://' + ip + ":" + port,
                   'user': user,
                   'database': db,
                   'basicAuth': False,
                   'isDefault': False,
                   'secureJsonData': {
                       'password': pw },
                    'version': 1,
                    'editable': True
            }]}

output_dir = "./grafana_datasources"
if not Path(output_dir).is_dir():
    os.mkdir(output_dir)
    print(datetime.now(), "Output directory \"" + str(output_dir) + "\" created!" )

for doc in compose_yaml:
    for service in doc['services']:
        if "influxdb" in doc['services'][service]['image']:
            name = doc['services'][service]['container_name']
            ip = args.ip
            port = doc['services'][service]['ports'][0].split(":")[0]
            for env in doc['services'][service]['environment']:
                if "INFLUXDB_DB" in env:
                    db = env.split("=")[1]
                elif "INFLUXDB_READ_USER=" in env:
                    user = env.split("=")[1]
                elif "INFLUXDB_READ_USER_PASSWORD" in env:
                    pw = env.split("=")[1]
            filename = name + ".yaml"
            f = open(output_dir + "/" + filename, "w")
            f.write(yaml.dump(yaml_template(name, ip, port, user, pw, db)))
            f.close()
            print(datetime.now(), "File \"" + filename + "\" written.")
