from abc import ABC, abstractmethod
from typing import Iterable

class RetailerConnector(ABC):
    """Contract for approved retailer data sources."""

    @abstractmethod
    def fetch_products(self) -> Iterable[dict]: ...

    @abstractmethod
    def fetch_product(self, external_id: str) -> dict | None: ...

    @abstractmethod
    def normalize_product(self, raw: dict) -> dict: ...

    @abstractmethod
    def fetch_price(self, external_id: str) -> dict: ...

    @abstractmethod
    def fetch_inventory(self, external_id: str) -> dict: ...

    @abstractmethod
    def health_check(self) -> bool: ...
