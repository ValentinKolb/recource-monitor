import asyncio

from fastapi import FastAPI

app = FastAPI()


async def ping(addr: str) -> dict:
    proc = await asyncio.create_subprocess_shell(
        f'ping -c 1 -W 1 {addr}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    return {
        "code": proc.returncode,
        "stdout": stdout.decode(),
        "stderr": stderr.decode()
    }


async def ping6(addr: str) -> dict:
    proc = await asyncio.create_subprocess_shell(
        f'ping6 -c 1 {addr}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    return {
        "code": proc.returncode,
        "stdout": stdout.decode(),
        "stderr": stderr.decode()
    }


@app.get("/ping/{addr}")
async def ping(addr: str):
    return await ping(addr)


@app.get("/ping6/{addr}")
async def ping(addr: str):
    return await ping6(addr)
