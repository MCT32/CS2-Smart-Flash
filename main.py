import asyncio
import kasa
from flask import Flask, request
import time

THRESHOLD = 127
HOST = "192.168.0.136"

DEVICE = None

async def async_setup():
    print("SETUPSETUPSETUPSETUPSETUPSETUPSETUPSETUPSETUPSETUPSETUP")
    global DEVICE
    DEVICE = await kasa.Discover.discover_single(HOST)

def create_app():
    app = Flask(__name__)

    with app.app_context():
        asyncio.run(async_setup())

    @app.route("/", methods=['POST'])
    async def hello_world():
        if not "player" in request.json:
            return ""
        if not "state" in request.json["player"]:
            return ""

        if "previously" in request.json:
            if "state" in request.json["previously"]:
                if request.json["player"]["state"]["flashed"] >= THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] < THRESHOLD:
                    await DEVICE.turn_on()
                    await DEVICE.update()
                    return ""
                if request.json["player"]["state"]["flashed"] < THRESHOLD and request.json["previously"]["player"]["state"]["flashed"] >= THRESHOLD:
                    await DEVICE.turn_off()
                    await DEVICE.update()
                    return ""
        
        if request.json["player"]["state"]["flashed"] >= THRESHOLD:
            await DEVICE.turn_on()
            await DEVICE.update()
        else:
            await DEVICE.turn_off()
            await DEVICE.update()

        return ""
    
    return app
