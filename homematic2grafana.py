#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from influxdb import InfluxDBClient
from pathlib import Path
import json
from  homematic2grafana_templates import dashboard_json, dashboard_target
from homematic_config import meas_config
from homematic2grafana_dashboardconfig import *

influx_ip = os.environ['influx_ip']
influx_port = os.environ['influx_port']
influx_user = os.environ['influx_user']
influx_pw = os.environ['influx_pw']
influx_db = os.environ['influx_db']

client = InfluxDBClient(host=influx_ip, port=influx_port, username=influx_user, password=influx_pw)
client.switch_database(influx_db)

output_dir = "./grafana_dashboards"
if not Path(output_dir).is_dir():
    os.mkdir(output_dir)
    print(datetime.now(), "Output directory \"" + str(output_dir) + "\" created!" )

measurements = client.get_list_measurements()
for measurement in measurements:
    m_name = measurement['name']
    if m_name in ignore_states:
        continue
    sum_values = client.query("SELECT count(*) as sum_count FROM " + m_name).get_points()
    for point in sum_values:
        for value in point:
            if "sum_count" in value:
                #print(m_name, point[value])
                continue
        if m_name in dashboard_values:
            fields = []
            fieldq = client.query("SHOW FIELD KEYS FROM " + m_name).get_points()
            for field in fieldq:
                fields.append(field['fieldKey'])
            entries = client.query("SHOW TAG VALUES FROM " + m_name + " WITH KEY = \"name\"").get_points()
            targets = []
            for entry in entries:
                #print(entry['value'])
                targets.append(dashboard_target(client, entry['value'], m_name, fields))
            filename = m_name + ".json"
            f = open(output_dir + "/" + filename, "w")
            kwargs = {}
            for option in dashboard_values[m_name]:
                kwargs[option] = dashboard_values[m_name][option]
                #print(option + "=" + str(dashboard_values[m_name][option]))
            f.write(json.dumps(dashboard_json(m_name, targets, **kwargs), indent=2, sort_keys=True))
            f.close()
            print(datetime.now(), "File \"" + filename + "\" written.")
client.close()
