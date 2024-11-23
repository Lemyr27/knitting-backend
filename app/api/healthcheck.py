from sqlalchemy import text

from app.utils import dependencies


async def healthcheck(db: dependencies.db_session) -> None:
    await db.execute(text("SELECT 1"))
