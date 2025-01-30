from collections import namedtuple
import json
from http import HTTPStatus

import aiohttp

from core.settings import settings

Response = namedtuple("response", ["status", "json"])


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
            data=json.dumps(
                {"deviceId": imei, "serviceId": settings.imeicheck_service_id},
            ),
        ) as response:
            return Response(response.status, await response.json())
    except aiohttp.ClientConnectorError as exc:
        return Response(HTTPStatus.SERVICE_UNAVAILABLE, str(exc))
