from grafana_client import GrafanaApi, TokenAuth


class Connect:
    def __init__(self, grafana_url: str, api_key: str):
        self.grafana_url = grafana_url
        self.api_key = api_key

    def connect(self) -> dict:
        grafana = GrafanaApi.from_url(
            url=self.grafana_url,
            credential=TokenAuth(token=self.api_key),
        )

        return grafana.health.check()
