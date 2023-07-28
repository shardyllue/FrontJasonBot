""" db """
from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncEngine,
    async_sessionmaker, AsyncSession,
)
from typing import Union
from sqlalchemy import URL


def create_engine(
    db_url : Union[str, URL],
) -> AsyncEngine:
    """
    
    Create async engine

    """

    return create_async_engine(
        url="postgresql+asyncpg://" + db_url
    )


def create_sessionmaker(
    engine : AsyncEngine
) -> AsyncSession:
    """
    
    Create async sessionmaker

    """

    return async_sessionmaker(
        bind=engine
    )