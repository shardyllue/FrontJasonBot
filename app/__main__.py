""" run async function """
from asyncio import run

from app.cli import client
from core import create_engine
from handler import ROUTERS

from utils import config



def startup():
    """
    
    Start up all process
    
    """

    engine = create_engine(config.PG_URL)

    try:
        run(client(
            engine=engine,
            routers=ROUTERS
        ))
    except KeyboardInterrupt:
        ...


if __name__ == "__main__":
    startup()