import asyncio
import kasa

async def main():
    dev = await kasa.Discover.discover_single("192.168.0.136")
    await dev.turn_off()
    await dev.update()

if __name__ == "__main__":
    asyncio.run(main())
