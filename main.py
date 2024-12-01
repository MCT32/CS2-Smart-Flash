import asyncio
import kasa
from flask import Flask, request
import time

THRESHOLD = 255

app = Flask(__name__)

@app.route("/", methods=['POST'])
async def hello_world():
    if request.json["player"]["state"]["flashed"]:
        if request.json["previously"]["player"]["state"]["flashed"]:
            if request.json["player"]["state"]["flashed"] >= THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] < THRESHOLD:
                dev = await kasa.Discover.discover_single("192.168.0.136")
                await dev.turn_on()
                await dev.update()
            if request.json["player"]["state"]["flashed"] < THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] >= THRESHOLD:
                dev = await kasa.Discover.discover_single("192.168.0.136")
                await dev.turn_off()
                await dev.update()
        else:
            if request.json["player"]["state"]["flashed"] >= THRESHOLD:
                dev = await kasa.Discover.discover_single("192.168.0.136")
                await dev.turn_on()
                await dev.update()
            else:
                dev = await kasa.Discover.discover_single("192.168.0.136")
                await dev.turn_off()
                await dev.update()

    return ""
