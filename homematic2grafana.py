#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
from datetime import datetime
import requests
from influxdb import InfluxDBClient
from pathlib import Path
import json
from  homematic2grafana_templates import dashboard_json, dashboard_target

influx_ip = os.environ['influx_ip']
influx_port = os.environ['influx_port']
influx_user = os.environ['influx_user']
influx_pw = os.environ['influx_pw']
influx_db = os.environ['influx_db']

print(datetime.now(), "starting...")
time_start = datetime.now()

client = InfluxDBClient(host=influx_ip, port=influx_port, username=influx_user, password=influx_pw)
client.switch_database(influx_db)

print(datetime.now(), "connected...")

dashboard_values = {
    'OPERATING_VOLTAGE': {},
    'LOWBAT': {},
    'ACTUAL_HUMIDITY': {},
    'ACTUAL_TEMPERATURE': {},
    'BATTERY_STATE': { 'yaxe1_format': 'volt'},
    'DUTYCYCLE': {},
    'DUTY_CYCLE': {},
    'HUMIDITY': {},
    'MOTION': { 'panel_bars': True, 'panel_lines': False },
    'TEMPERATURE': { 'yaxe1_format': 'celsius'},
    'WINDOW_STATE': {}
}

output_dir = "./grafana_dashboards"
if not Path(output_dir).is_dir():
    os.mkdir(output_dir)
    print(datetime.now(), "Output directory \"" + str(output_dir) + "\" created!" )

measurements = client.get_list_measurements()
for measurement in measurements:
    m_name = measurement['name']
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
                targets.append(dashboard_target(entry['value'], m_name, fields))
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

print(datetime.now(), "finished...")
time_end = datetime.now()
print("duration: ", time_end-time_start)