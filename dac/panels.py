
class PanelLibrary:
    def __init__(self):
        pass
        # self.grafana_url = grafana_url
        # self.api_key = api_key

    def cpu_panel(self) -> dict:
        cpu_panel = {
                    "type": "graph",
                    "title": "CPU Usage",
                    "datasource": "Prometheus",

                    "targets": [
                        {
                            "expr": "node_cpu_seconds_total{namespace='monitoring'}",
                            "legendFormat": "{{pod}}",
                            "refId": "A"
                        }
                    ],
                    "gridPos": {"x": 0, "y": 0, "w": 6, "h": 6}
                }
        return cpu_panel

    def mem_panel(self) -> dict:
        mem_panel = {
                    "type": "graph",
                    "title": "Mem Usage",
                    "datasource": "Prometheus",

                    "targets": [
                        {
                            "expr": "node_cpu_seconds_total{namespace='monitoring'}",
                            "legendFormat": "{{pod}}",
                            "refId": "A"
                        }
                    ],
                    "gridPos": {"x": 6, "y": 0, "w": 6, "h": 6}
                }
        return mem_panel

    def net_panel(self) -> dict:
        net_panel = {
                    "type": "stat",
                    "title": "Network Usage",
                    "datasource": "Prometheus",

                    "targets": [
                        {
                            "expr": "up{namespace='monitoring', service='prometheus'}",
                            "legendFormat": "{{pod}}",
                            "refId": "A"
                        }
                    ],
                    "gridPos": {"x": 12, "y": 6, "w": 6, "h": 6}
                }
        return net_panel
