FROM python:slim

# Image Description
LABEL version="1.0" description="Script to Query Homematic data and store it to InfluxDB"

# Install required Python Modules
RUN pip install influxdb requests

# Install pgrep for stopping the Python Script in case needed
RUN apt-get update && apt-get install -y procps htop dos2unix && apt-get autoremove && apt-get clean

# Define Environment Variables needed for Script
ENV hm_ip="192.168.1.5" influx_ip="192.168.1.3" influx_port="8086" influx_user="user" influx_pw="pw" influx_db="homematic" interval="60"

# Set correct Timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

# Copy Scriptis to Container
ADD ./homematic.py /homematic.py
RUN chmod +x /homematic.py
RUN dos2unix /homematic.py
RUN mkdir /grafana_dashboards
ADD ./homematic2grafana_list.py /homematic2grafana_list.py
ADD ./homematic2grafana.py /homematic2grafana.py
ADD ./homematic2grafana_templates.py /homematic2grafana_templates.py

# Default Command for starting the Container
CMD ["/homematic.py"]