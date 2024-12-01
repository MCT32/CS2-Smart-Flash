import asyncio
import kasa
from flask import Flask

from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
async def hello_world():
    dev = await kasa.Discover.discover_single("192.168.0.136")
    await dev.turn_on()
    await dev.update()

    time.sleep(0.5)

    await dev.turn_off()
    await dev.update()

    return ""
