import asyncio
from pykit.log import log
from typing import Self
import aioconsole

class App:
    @classmethod 
    async def run(cls):
        app = await App().init()
        await app.serve()

    async def init(self) -> Self:
        return self

    async def serve(self):
        while True:
            inp = await aioconsole.ainput()
            print(inp)

