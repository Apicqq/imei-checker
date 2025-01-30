from http import HTTPStatus

import aiohttp
from fastapi.exceptions import HTTPException

from api_app.schemas import ImeiIn
from core.settings import settings
from utils.imei_verification import check_imei

async def verify_imei(body: ImeiIn, session: aiohttp.ClientSession) -> dict:
    if body.token != settings.api_token:
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED,
            "Invalid API token"
        )
    return await check_imei(body.imei, session)
