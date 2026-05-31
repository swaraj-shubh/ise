import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
database_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://admin:admin123@localhost:5432/mydatabase")
if database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

database_url_base = database_url.split("?")[0]
if "sslmode=require" in database_url:
    engine = create_async_engine(database_url_base, connect_args={"ssl": "require"}, pool_pre_ping=True, pool_recycle=300)
else:
    engine = create_async_engine(database_url_base, pool_pre_ping=True, pool_recycle=300)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session() as session:
        yield session