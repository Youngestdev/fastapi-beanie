from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional


class ProductReview(Document):
    id: UUID = Field(alias="_id", default_factory=uuid4)
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "products"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Abdulazeez",
                "product": "TestDriven TDD Course",
                "rating": 4.9,
                "review": "Excellent course!",
                "date": datetime.now()
            }
        }


class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez",
                "product": "TestDriven TDD Course",
                "rating": 5.0,
                "review": "Excellent course!",
                "date": datetime.now()
            }
        }
