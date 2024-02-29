from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview


async def init_db():

    DATABASE_URL = "mongodb://dev:dev@localhost:27018/?authSource=admin"

    client = AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")

    db = client["reviews"]

    await init_beanie(database=db, document_models=[ProductReview])
