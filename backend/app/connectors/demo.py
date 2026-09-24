from .base import RetailerConnector

class DemoRetailerConnector(RetailerConnector):
    """Synthetic connector. It does not call any real retailer."""

    def __init__(self, rows: list[dict]):
        self.rows = rows

    def fetch_products(self):
        return iter(self.rows)

    def fetch_product(self, external_id: str):
        return next((x for x in self.rows if x.get("external_id") == external_id), None)

    def normalize_product(self, raw: dict):
        return dict(raw, source_type="synthetic_demo")

    def fetch_price(self, external_id: str):
        row = self.fetch_product(external_id) or {}
        return {"price": row.get("price"), "synthetic": True}

    def fetch_inventory(self, external_id: str):
        row = self.fetch_product(external_id) or {}
        return {"sizes": row.get("sizes", []), "synthetic": True}

    def health_check(self):
        return True
