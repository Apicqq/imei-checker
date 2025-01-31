import asyncio
from dataclasses import dataclass
from http import HTTPStatus

import aiohttp

from core.settings import settings

@dataclass(frozen=True)
class Response:
    """Class for representing response from external API call."""

    status: int
    data: dict | str


async def check_imei(imei: str, session: aiohttp.ClientSession) -> Response:
    """
    Verify IMEI.

    Gathers data from external API service and returns it.
    :param imei: IMEI of the device.
    :param session: session to be used.
    :return: Response object, which consists of status code and JSON data.
    """
    try:
        async with session.post(
            settings.imeicheck_url,
            headers={
                "Authorization": f"Bearer {settings.imeicheck_token}",
                "Content-Type": "application/json",
            },
            json={
                "deviceId": imei, "serviceId": settings.imeicheck_service_id,
            },
        ) as response:
            return Response(response.status, await response.json())
    except aiohttp.ClientError as exc:
        return Response(HTTPStatus.SERVICE_UNAVAILABLE, str(exc))
    except asyncio.TimeoutError as exc:
        return Response(HTTPStatus.GATEWAY_TIMEOUT, str(exc))
