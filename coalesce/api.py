"""User facing coalesce API"""
from aiohttp import ClientResponseError
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from .fetch import get_coverages
from .models import Coverage, Strategy
from .strategies import STRATEGIES

api = FastAPI()


@api.get("/")
async def coalesce(member_id: int, strategy: Strategy = Strategy.average) -> Coverage:
    """Coalesce the coverages for a member using the given strategy"""
    try:
        coverages = await get_coverages(member_id)
    # Catch the exceptions we can reasonably anticipate
    except ClientResponseError:
        raise HTTPException(status_code=424, detail="Failed to get upstream data")
    except ValidationError:
        raise HTTPException(status_code=424, detail="Upstream data is malformed")

    return STRATEGIES[strategy.value](coverages)
