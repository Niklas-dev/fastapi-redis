from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.cache import cache_dependency
from app.db.database import db_dependency
from app.routers.data.models import Data

router = APIRouter(
    prefix='/data',
    tags=['data']
)


class GetDataRequest(BaseModel):
    id: int


class PostDataRequest(BaseModel):
    value: str


@router.get("/")
def get_data(data_request: GetDataRequest, db: db_dependency, cache: cache_dependency):
    # Try to get data from the cache
    cached_data = cache.get(data_request.key)
    if cached_data:
        print("returned from cache")
        return {"data": cached_data}

    # If not in cache, get data from the database
    data = db.query(Data).filter(Data.id == data_request.id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    # Store data in cache for future requests
    cache.set(data_request.key, data.value)
    print("returned from db")
    return {"data": data.value}


@router.post("/")
def post_data(data_request: PostDataRequest, db: db_dependency):
    data = Data(value=data_request.value)
    db.add(data)
    db.commit()
    db.refresh(data)
    return "Added data"
