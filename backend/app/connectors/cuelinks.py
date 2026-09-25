import os
from typing import Any

import httpx
from fastapi import HTTPException

BASE_URL = os.getenv("CUELINKS_BASE_URL", "https://developers.cuelinks.com/pub_api/v3")
API_KEY = os.getenv("CUELINKS_API_KEY")


async def request(method: str, path: str, **kwargs: Any):
    if not API_KEY:
        raise HTTPException(status_code=503, detail="CUELINKS_API_KEY is not configured on the server")
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Token {API_KEY}"
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.request(method, f"{BASE_URL}{path}", headers=headers, **kwargs)
    if response.status_code >= 400:
        raise HTTPException(status_code=response.status_code, detail=response.text[:500])
    return response.json()
