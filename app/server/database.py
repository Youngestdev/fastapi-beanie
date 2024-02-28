from beanie import init_beanie
import motor.motor_asyncio

from server.models.product_review import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://dev:dev@localhost:27018/productreviews?authSource=admin&readPreference=primary&appname=Pyservice&directConnection=true&ssl=false"
    )

    await init_beanie(database=client.db_name, document_models=[ProductReview])
