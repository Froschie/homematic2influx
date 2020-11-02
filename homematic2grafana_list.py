#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from influxdb import InfluxDBClient
import argparse

influx_ip = os.environ['influx_ip']
influx_port = os.environ['influx_port']
influx_user = os.environ['influx_user']
influx_pw = os.environ['influx_pw']
influx_db = os.environ['influx_db']

parser=argparse.ArgumentParser(
    description='''Script for listing the Influx DB entries of Homematic Devices.''')
parser.add_argument('--fields', required=False, action='store_true', help='Show details on table fields.')
parser.add_argument('--devices', required=False, action='store_true', help='Show details on devices in table.')
args=parser.parse_args()

client = InfluxDBClient(host=influx_ip, port=influx_port, username=influx_user, password=influx_pw)
client.switch_database(influx_db)

measurements = client.get_list_measurements()
sum_measurements = 0
print("Measurements:")
for measurement in measurements:
    m_name = measurement['name']
    sum_values = client.query("SELECT count(*) as sum_count FROM " + m_name).get_points()
    for point in sum_values:
        for value in point:
            if "sum_count" in value:
                print("  " + str(m_name) + ", Points: " + str(point[value]))
                sum_measurements += point[value]
    if args.fields:
        fields = client.query("SHOW FIELD KEYS FROM " + m_name).get_points()
        for field in fields:
            sum_count = ""
            sum_values = client.query("SELECT count(" + field['fieldKey'] + ") as sum_count FROM " + m_name).get_points()
            for point in sum_values:
                    for value in point:
                        if "sum_count" in value:
                            sum_count = str(point[value])
            print("    " + str(field['fieldKey']) + " (Field), Points: " + sum_count)
    if args.devices:
        entries = client.query("SHOW TAG VALUES FROM " + m_name + " WITH KEY = \"name\"").get_points()
        for entry in entries:
            sum_count = ""
            sum_values = client.query("SELECT count(*) as sum_count FROM " + m_name + " WHERE (\"name\" = '" + entry['value']  + "')").get_points()
            for point in sum_values:
                    for value in point:
                        if "sum_count" in value:
                            sum_count = str(point[value])
            print("      " + str(entry['value']) + " (Device), Points: " + sum_count)
client.close()

print("Summary:")
print("  Measurements:", sum_measurements)
