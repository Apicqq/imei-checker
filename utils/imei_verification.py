import json

import aiohttp

async def check_imei(imei: str, session: aiohttp.ClientSession) -> dict:
    try:
        async with session.post(
                "https://api.imeicheck.net/v1/checks",
                headers={
                    "Authorization": "Bearer e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "deviceId": imei,
                    "serviceId": 12
                })
        ) as response:
            if response.status != 201:
                return {"error": await response.text()}
            return await response.json()
    except aiohttp.ClientConnectorError as exc:
        return {"error": str(exc)}