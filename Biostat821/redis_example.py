"""HTTP API."""
import asyncio
import redis

from fastapi import FastAPI

app = FastAPI()

# cache = dict()

@app.get("/slowly_multiply")
async def take_a_long_time(a: int, b: int) -> int:
    """Get something, taking a long time."""
    cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

    key = hash((a, b))
    if cache.exists(key):
        return cache.get(key)

    await asyncio.sleep(10)
    value = a * b

    cache.set(key, value)
    return value

if __name__ == "__main__":
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # r.set("a", 123)
    print(r.get("a"))