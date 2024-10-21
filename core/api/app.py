import json
from http import HTTPStatus
from fastapi import FastAPI, Response
from api.schemas import Result
from redis import Redis
from asyncio import sleep
from random import randint

app = FastAPI(docs_url=None, redoc_url=None)
rd = Redis(host="redis", port=6379, db=0)


async def slow_process():
    """
    Simulates a slow process by asynchronously sleeping for a random time between 3 to 6 seconds.
    
    Returns:
        dict: A dictionary indicating that the slow process has finished.
    """
    await sleep(randint(3, 6))
    return {"slow_process": "finished"}


@app.get("/no-cache", response_model=Result, status_code=HTTPStatus.OK)
async def get_response_no_cache():
    """
    Endpoint to get a response without caching.
    
    This endpoint triggers a slow process and returns the result without any caching mechanism.
    If an exception occurs, it returns a BAD_REQUEST response.
    
    Returns:
        Result: A response model containing the result of the slow process.
    """

    try:       
        result = await slow_process()
        return Result(success=result)

    except Exception as e:
        return Response(
            status_code=HTTPStatus.BAD_REQUEST,
            content=Result(erro=f"{e}").model_dump_json(),
        )

@app.get("/cache-redis", response_model=Result, status_code=HTTPStatus.OK)
async def get_response_redis():
    """
    Endpoint to get a response with Redis caching.
    
    This endpoint triggers a slow process and stores the result in Redis cache for 60 seconds.
    If the cached result exists, it returns the cached response instead of processing again.
    If an exception occurs, it returns a BAD_REQUEST response.
    
    Returns:
        Result: A response model containing the result of the slow process, either from cache or by executing the process.
    """

    try:
        key = "Cache-Response"
        if cache := rd.get(key):
            return Result(success=json.loads(cache))

        else:
            result = await slow_process()

            rd.set(key, json.dumps(result))
            rd.expire(key, time=60)

        return Result(success=result)

    except Exception as e:
        return Response(
            status_code=HTTPStatus.BAD_REQUEST,
            content=Result(erro=f"{e}").model_dump_json(),
        )
