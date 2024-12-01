import asyncio
import kasa
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/", methods=['POST'])
async def hello_world():
    if request.json["player"]["state"]["flashed"]:
        if request.json["player"]["state"]["flashed"] >= 255:
            dev = await kasa.Discover.discover_single("192.168.0.136")
            await dev.turn_on()
            await dev.update()
        else:
            dev = await kasa.Discover.discover_single("192.168.0.136")
            await dev.turn_off()
            await dev.update()

    return ""
