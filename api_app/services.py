from http import HTTPStatus

import aiohttp
from fastapi.exceptions import HTTPException

from api_app.schemas import ImeiIn, ImeiOut
from core.settings import settings
from utils.imei_verification import check_imei, Response


async def verify_imei(body: ImeiIn, session: aiohttp.ClientSession) -> ImeiOut:
    """
    Service function to verify IMEI.

    Contains all the business logic and verifications needed to
    run the verification process.
    """
    if body.token != settings.api_token:
        raise HTTPException(HTTPStatus.UNAUTHORIZED, "Invalid API token")
    result: Response = await check_imei(body.imei, session)
    if result.status != HTTPStatus.CREATED:
        raise HTTPException(result.status, result.json)
    return ImeiOut(status=result.status, result=result.json)
