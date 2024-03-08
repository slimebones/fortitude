import asyncio
import os
import sys
from pykit.log import log
from pykit.env import EnvUtils
from typing import Self
from loguru import logger as _logger
import aioconsole

class App:
    @classmethod 
    async def run(cls):
        app = await App().init()
        await app.serve()

    async def init(self) -> Self:
        env_debug = EnvUtils.get_bool("FORT_DEBUG", "1")
        self._is_debug = env_debug
        log.is_debug = env_debug

        _logger.remove(0)
        log_format = \
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |" \
            " <level>{level: <8}</level> - <level>{message}</level>"
        _logger.add(sys.stdout, format=log_format)

        return self

    async def serve(self):
        while True:
            inp = await aioconsole.ainput()
            print(inp)

