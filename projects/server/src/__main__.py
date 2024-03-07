import asyncio

from pykit.log import log
from src.app import App

async def main():
    await App.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("received keyboard interrupt")
        exit(0)

