from pydantic import BaseModel, Field
from typing import Optional

class Offer(BaseModel):
    retailer: str
    price: int
    mrp: int
    sizes: list[str]
    url: Optional[str] = None
    synthetic: bool = True

class Product(BaseModel):
    id: str
    brand: str
    title: str
    gender: str
    category: str
    article_type: str
    colour: str
    fit: Optional[str] = None
    fabric: Optional[str] = None
    attributes: dict[str, str] = Field(default_factory=dict)
    offers: list[Offer]
    similar_product_ids: list[str] = Field(default_factory=list)

class MatchCandidate(BaseModel):
    left_listing_id: str
    right_listing_id: str
    exact_identifier_score: float = 0
    structured_score: float = 0
    semantic_score: float = 0
    image_score: float = 0
