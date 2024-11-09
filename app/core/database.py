from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.settings import app_settings

url = URL.create(
    'postgresql+asyncpg',
    app_settings.DB_USER,
    app_settings.DB_PASS,
    app_settings.DB_HOST,
    app_settings.DB_PORT,
    app_settings.DB_NAME,
)

async_engine = create_async_engine(url)
async_session = async_sessionmaker(async_engine)


class BaseModel(DeclarativeBase, AsyncAttrs):
    id: Mapped[int] = mapped_column(primary_key=True)


async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session
