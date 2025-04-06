import asyncio
from app.db import engine
from app.models.base import Base
from app.models import user, domain, lookup, history  # make sure these are imported

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Run if script is called directly
if __name__ == "__main__":
    asyncio.run(init_db())
