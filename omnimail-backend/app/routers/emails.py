from fastapi import APIRouter

router = APIRouter()


@router.get("/emails")
def get_emails():
    return {"message":"Here are all the emails"}


@router.get("/emails/{email_id}")
def get_email(email_id:int):
    return {"message":f"here you see email with ID :{email_id}"}