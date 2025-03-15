from dac.grafana import Connect
from dac.panels import PanelLibrary as pl
from grafana_client import GrafanaApi, TokenAuth
import os

# Connect to Grafana API endpoint using the `GrafanaApi` class
# Grafana server details
GRAFANA_URL = "http://localhost:3000"
API_KEY = os.getenv("GRAFANA_API_KEY")

# grafana_connect = Connect(GRAFANA_URL, API_KEY)
# print(grafana_connect.connect())
#
# new = grafana_connect.dashboard.update_dashboard("new")

grafana = GrafanaApi.from_url(
            url=GRAFANA_URL,
            credential=TokenAuth(token=API_KEY),
            timeout=10000,
        )

print(grafana.health.check())

# cpu_panel = {
#         "type": "graph",
#         "title": "CPU Usage",
#         "datasource": "Prometheus",

#         "targets": [
#             {
#                 "expr": "node_cpu_seconds_total{namespace='monitoring'}",
#                 "legendFormat": "{{pod}}",
#                 "refId": "A"
#             }
#         ],
#         "gridPos": {"x": 0, "y": 0, "w": 6, "h": 6}
#         }

# mem_panel = {
#         "type": "graph",
#         "title": "Memory Usage",
#         "datasource": "Prometheus",

#         "targets": [
#             {
#                 "expr": "node_cpu_seconds_total{namespace='monitoring'}",
#                 "legendFormat": "{{pod}}",
#                 "refId": "A"
#             }
#         ],
#         "gridPos": {"x": 6, "y": 0, "w": 6, "h": 6}
#         }
# net_panel = {
#         "type": "stat",
#         "title": "Network Usage",
#         "datasource": "Prometheus",

#         "targets": [
#             {
#                 "expr": "up{namespace='monitoring'}",
#                 "legendFormat": "{{pod}}",
#                 "refId": "A"
#             }
#         ],
#         "gridPos": {"x": 12, "y": 6, "w": 6, "h": 6}
#         }

dashboard_payload = {
    "dashboard": {
        "id": None,  # Creates a new dashboard
        "uid": "new_dashboard_uid",
        "title": "K8S MLT view Dashboard",
        "panels": [pl.cpu_panel("cpu"), pl.mem_panel("mem"), pl.net_panel("net")],
        "timezone": "browser",
    },
    "overwrite": True
}



response = grafana.dashboard.update_dashboard(dashboard_payload)
print("Dashboard Created:", response["uid"])
