#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-

import time
import os
from datetime import datetime, timedelta
import requests
import xml.etree.ElementTree as ET
from influxdb import InfluxDBClient
from homematic_config import *

influx_ip = os.environ['influx_ip']
influx_port = os.environ['influx_port']
influx_user = os.environ['influx_user']
influx_pw = os.environ['influx_pw']
influx_db = os.environ['influx_db']
hm_ip = os.environ['hm_ip']
interval = float(os.environ['interval'])

url = "http://" + hm_ip + "/addons/xmlapi/"

def value(value, type):
    if int(type) == 16:
        # change to float
        return float(value)
    elif int(type) == 4 or int(type) == 6:
        return float(value)
    elif int(type) == 8:
        # change to float
        return float(value)
    elif int(type) == 2:
        # change bool value to float
        if str(value) == "false":
            return float(0)
        else:
            return float(1)
    else:
        return str(value)

def influx_json(node_type_meas, dev_type, node_timestamp, dev_name, node_type, node_value, node_valuetype):
    return {
        "measurement": str(node_type_meas),
        "time": int(node_timestamp),
        "tags": {
            "name": str(dev_name),
            "device_type": str(dev_type)
        },
        "fields": {
            str(node_type): value(node_value, node_valuetype)
        }
    }

# Time Rounding Function
def ceil_time(ct, delta):
    return ct + (datetime.min - ct) % delta

client = InfluxDBClient(host=influx_ip, port=influx_port, username=influx_user, password=influx_pw)
client.switch_database(influx_db)

new_time = ceil_time(datetime.now(), timedelta(seconds=int(interval)))

try:
    while True:
        time_start = datetime.now()
        print(datetime.now(), "Querying Homematic Data...")

        dev_list = ET.fromstring(requests.get(url + 'devicelist.cgi').text)
        devices = {}
        for dev in dev_list:
            devices[dev.attrib['ise_id']] = {'name': dev.attrib['name'], 'address': dev.attrib['address'], 'interface': dev.attrib['interface'], 'device_type': dev.attrib['device_type']}

        state_list = ET.fromstring(requests.get(url + 'statelist.cgi').text)

        json_body = []

        for dev in state_list:
            if dev.attrib['ise_id'] in devices:
                dev_type = devices[dev.attrib['ise_id']]['device_type']
            else:
                continue
            if dev_type not in ignore_devices:
            #if dev.attrib['device_type'] in test_sensor:
                #print(dev.tag, dev.attrib)
                for node in dev.iter():
                    if node.tag == "datapoint":
                        n_type = node.attrib['type']
                        channel_no = node.attrib['name'].split(":")[1].split(".")[0]
                        if int(channel_no) > 0:
                            node_type = n_type + "_" + str(channel_no)
                        else:
                            node_type = n_type
                        #print(node.tag, node.attrib['type'], value(node.attrib['value'], node.attrib['valuetype']), node.attrib['timestamp'])
                        if int(node.attrib['timestamp']) > 0 and n_type not in ignore_states:
                            if n_type in meas_config:
                                if 'meas_remap' in meas_config[n_type]:
                                    n_type = meas_config[n_type]['meas_remap']
                                if 'field_remap' in meas_config[n_type]:
                                    if node_type in meas_config[n_type]['field_remap']:
                                        node_type = meas_config[n_type]['field_remap'][node_type]
                            json_body.append(influx_json(n_type, dev_type, node.attrib['timestamp'], dev.attrib['name'], node_type, node.attrib['value'], node.attrib['valuetype']))

        sysvar_list = ET.fromstring(requests.get(url + 'sysvarlist.cgi').text)
        sysvars = {}
        for sysvar in sysvar_list:
            if int(sysvar.attrib['timestamp']) > 1000000000:
                json_body.append(influx_json("SYSTEM_VARS", "systemVariable", sysvar.attrib['timestamp'], sysvar.attrib['name'], sysvar.attrib['name'].replace(" ", "_"), sysvar.attrib['value'], sysvar.attrib['type']))

        influx_result = client.write_points(json_body, time_precision='s')
        if influx_result:
            print(datetime.now(), "InfluxDB write data successfull:", len(json_body))
        else:
            print(datetime.now(), "InfluxDB write data FAILED:" + str(json_body))
            print(influx_result)

        time_end = datetime.now()
        print(datetime.now(), "Cycle completed in:", time_end-time_start)

        time.sleep(interval - ((time.time() - new_time.timestamp()) % interval))
except KeyboardInterrupt:
    print("Script aborted...")
finally:
    client.close()
