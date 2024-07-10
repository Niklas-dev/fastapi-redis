from fastapi import APIRouter


router = APIRouter(
    prefix='/data',
    tags=['data']
)


@router.get("/data")
def get_data(request):
    return ""