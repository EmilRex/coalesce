"""Testing API for serving upstream data"""
from fastapi import FastAPI, HTTPException

api = FastAPI()

# {api_id: {member_id: (deductible, stop_loss, oop_max)}}
data = {
    1: {
        1: (100, 100, 100),
        2: (200, 200, 200),
        3: (-300, -300, -300),
    },
    2: {
        1: (100, 200, 300),
        2: (400, 500, 600),
        3: (-700, -800, -900),
    },
    3: {
        1: (100, 200, 300),
        2: (100, 200, 300),
        3: (100, 200, 300),
    },
}


@api.get("/api/{api_id}")
async def get_data(api_id: int, member_id: int) -> dict:
    """Return the testing data or 404"""
    if api_id not in data.keys():
        raise HTTPException(status_code=404, detail="API not found")

    if member_id not in data[api_id].keys():
        raise HTTPException(status_code=404, detail="Member not found")

    deductible, stop_loss, oop_max = data[api_id][member_id]
    return {
        "deductible": deductible,
        "stop_loss": stop_loss,
        "oop_max": oop_max
    }
