"""Asynchronous upstream data fetching functions"""
import asyncio
import os

import aiohttp

from .models import Coverage

urls = os.environ["COALESCE_UPSTREAM_API_URLS"].split(",")


async def get_coverage(session, url: str, params: dict):
    """Fetches and validates member data for a single upstream source"""
    async with session.get(url, params=params, raise_for_status=True) as resp:
        data = await resp.json()
        return Coverage(**data)


async def get_coverages(member_id: int, urls: list[str] = urls):
    """Fetches and validates member data asynchronously across upstream sources"""
    async with aiohttp.ClientSession() as session:
        params = {"member_id": member_id}
        tasks = [asyncio.ensure_future(get_coverage(session, url, params)) for url in urls]
        coverages = await asyncio.gather(*tasks)
        return coverages
