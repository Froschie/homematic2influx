def dashboard_fields(client, fields, measurement, name):
    temp_fields = []
    for field in fields:
        sum_values = client.query("SELECT count(" + field + ") as sum_count FROM " + measurement + " WHERE (\"name\" = '" + name  + "')").get_points()
        for point in sum_values:
            for value in point:
                if "sum_count" in value:
                    temp_fields.append([
            {
                "params": [
                    field
                ],
                "type": "field"
            }
        ])
    return temp_fields

def dashboard_target(client, name, measurement, fields):
    return {
                "alias": name,
                "groupBy": [],
                "measurement": measurement,
                "orderByTime": "ASC",
                "policy": "default",
                "resultFormat": "time_series",
                "select": dashboard_fields(client, fields, measurement, name),
                "tags": [
                    {
                        "key": "name",
                        "operator": "=",
                        "value": name
                    }
                ],
                "tz": "Europe/Berlin"
            }

def dashboard_json(name, targets, **kwargs):
    # default values
    dv = {
        'yaxe1_format': 'short',
        'yaxe2_format': 'short',
        'panel_bars': False,
        'panel_lines': True,
        'panel_stack': False,
        'panel_steppedLine': False
    }
    # take values from arguments
    for key, value in kwargs.items():
        dv[key] = value
    return {
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": "-- Grafana --",
                    "enable": True,
                    "hide": True,
                    "iconColor": "rgba(0, 211, 255, 1)",
                    "name": "Annotations & Alerts",
                    "type": "dashboard"
                }
            ]
        },
        "editable": True,
        "gnetId": None,
        "graphTooltip": 0,
        "links": [],
        "panels": [
            {
                "aliasColors": {},
                "bars": dv['panel_bars'],
                "dashLength": 10,
                "dashes": False,
                "datasource": "inf_homematic",
                "fieldConfig": {
                    "defaults": {
                        "custom": {}
                    },
                    "overrides": []
                },
                "fill": 0,
                "fillGradient": 0,
                "gridPos": {
                    "h": 17,
                    "w": 24,
                    "x": 0,
                    "y": 0
                },
                "hiddenSeries": False,
                "id": 2,
                "legend": {
                    "avg": False,
                    "current": False,
                    "max": False,
                    "min": False,
                    "show": True,
                    "total": False,
                    "values": False
                },
                "lines": dv['panel_lines'],
                "linewidth": 1,
                "NonePointMode": "None",
                "options": {
                    "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "7.3.1",
                "pointradius": 2,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": dv['panel_stack'],
                "steppedLine": dv['panel_steppedLine'],
                "targets": targets,
                "thresholds": [],
                "timeFrom": None,
                "timeRegions": [],
                "timeShift": None,
                "title": name,
                "tooltip": {
                    "shared": True,
                    "sort": 0,
                    "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                    "buckets": None,
                    "mode": "time",
                    "name": None,
                    "show": True,
                    "values": []
                },
                "yaxes": [
                    {
                        "format": dv['yaxe1_format'],
                        "label": None,
                        "logBase": 1,
                        "max": None,
                        "min": None,
                        "show": True
                    },
                    {
                        "format": dv['yaxe2_format'],
                        "label": None,
                        "logBase": 1,
                        "max": None,
                        "min": None,
                        "show": True
                    }
                ],
                "yaxis": {
                    "align": False,
                    "alignLevel": None
                }
            }
        ],
        "refresh": "1m",
        "schemaVersion": 26,
        "style": "dark",
        "tags": [],
        "templating": {
            "list": []
        },
        "time": {
            "from": "now-24h",
            "to": "now"
        },
        "timepicker": {},
        "timezone": "",
        "title": name,
        "uid": name,
        "version": 1
    }
