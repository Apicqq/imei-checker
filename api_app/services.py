import aiohttp

from fastapi.exceptions import HTTPException

from api_app.schemas import ImeiIn
from utils.imei_verification import check_imei

async def verify_imei(body: ImeiIn, session: aiohttp.ClientSession) -> dict:
    if body.token != "132fdsfsd":
        raise HTTPException(
            401,
            "Invalid API token"
        )
    return await check_imei(body.imei, session)