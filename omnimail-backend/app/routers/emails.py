from fastapi import APIRouter
from fastapi import HTTPException
from app.models.models import Email

router = APIRouter()


fake_emails = [
    Email(subject="Meeting Reminder", sender="boss@example.com", body="Don't forget the meeting!", timestamp="2025-05-01T10:00:00", is_read=False),
    Email(subject="Project Update", sender="colleague@example.com", body="Here is the project update.", timestamp="2025-05-01T12:00:00", is_read=True),
]

@router.get("/emails",response_model=list[Email])
def get_emails():
    return fake_emails


@router.get("/emails/{email_id}",response_model=Email)
def get_email(email_id:int):
    try:
        return fake_emails[email_id]
    except IndexError:
        raise HTTPException(status_code=404,detail=F"Email with id {email_id} not found")
    