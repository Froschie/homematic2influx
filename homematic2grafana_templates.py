def dashboard_fields(fields):
    temp_fields = []
    for field in fields:
        temp_fields.append([
            {
                "params": [
                    field
                ],
                "type": "field"
            }
        ])
    return temp_fields

def dashboard_target(name, measurement, fields):
    return {
                "alias": name,
                "groupBy": [],
                "measurement": measurement,
                "orderByTime": "ASC",
                "policy": "default",
                "resultFormat": "time_series",
                "select": dashboard_fields(fields),
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
    yaxe1_format='short'
    yaxe2_format='short'
    panel_bars=False
    panel_lines=True
    # take values from arguments
    for key, value in kwargs.items():
        key = value
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
                "bars": panel_bars,
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
                "lines": panel_lines,
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
                "stack": False,
                "steppedLine": False,
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
                        "format": yaxe1_format,
                        "label": None,
                        "logBase": 1,
                        "max": None,
                        "min": None,
                        "show": True
                    },
                    {
                        "format": yaxe2_format,
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
