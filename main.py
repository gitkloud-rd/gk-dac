import os
from grafana_client import GrafanaApi, TokenAuth

from dac.grafana import Connect
from dac.panels import PanelLibrary as pl

# Connect to Grafana API endpoint using the `GrafanaApi` class
GRAFANA_URL = "http://localhost:3000"
API_KEY = os.getenv("GRAFANA_API_KEY")

grafana = GrafanaApi.from_url(
            url=GRAFANA_URL,
            credential=TokenAuth(token=API_KEY),
            timeout=10000,
        )

print(grafana.health.check())

dashboard_payload = {
    "dashboard": {
        "id": None,  # Creates a new dashboard
        "uid": "new_dashboard_uid",
        "title": "K8S MLT view Dashboard",
        "panels": [pl.cpu_panel("cpu"), pl.mem_panel("mem"), pl.net_panel("net")],
        "timezone": "browser",
    },
    "tags": ["k8s", "mlt"],
    "overwrite": True
}

response = grafana.dashboard.update_dashboard(dashboard_payload)
print("Dashboard Created:", response["uid"])
