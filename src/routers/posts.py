from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return [
        {
            "id": 1,
            "title": "Test title",
            "description": "Test post description",
        },
        {
            "id": 2,
            "title": "Test title",
            "description": "Test post description",
        },
    ]


@router.get("/{post_id}")
def read_post(post_id: int):
    return {
        "post_id": post_id,
        "title": "Test title",
        "description": "Test post description",
    }
