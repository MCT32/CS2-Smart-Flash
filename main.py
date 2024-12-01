import asyncio
import kasa
from flask import Flask, request
import time

THRESHOLD = 255
HOST = "192.168.0.136"

app = Flask(__name__)

@app.route("/", methods=['POST'])
async def hello_world():
    if not "player" in request.json:
        return ""
    if not "state" in request.json["player"]:
        return ""

    if "previously" in request.json:
        if "state" in request.json["previously"]:
            if request.json["player"]["state"]["flashed"] >= THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] < THRESHOLD:
                dev = await kasa.Discover.discover_single(HOST)
                await dev.turn_on()
                await dev.update()
                return ""
            if request.json["player"]["state"]["flashed"] < THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] >= THRESHOLD:
                dev = await kasa.Discover.discover_single(HOST)
                await dev.turn_off()
                await dev.update()
                return ""
    
    if request.json["player"]["state"]["flashed"] >= THRESHOLD:
        dev = await kasa.Discover.discover_single(HOST)
        await dev.turn_on()
        await dev.update()
    else:
        dev = await kasa.Discover.discover_single(HOST)
        await dev.turn_off()
        await dev.update()

    return ""
