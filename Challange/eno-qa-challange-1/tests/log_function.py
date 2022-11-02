import logging
import asyncio


async def log_to_stdout():
    while True:
        logging.warning('This line should be logged every 1 minute')
        await asyncio.sleep(60)


if __name__ == "__main__":
    try:
        asyncio.run(log_to_stdout())
    except KeyboardInterrupt:
        logging.warning('Canceled by user')
