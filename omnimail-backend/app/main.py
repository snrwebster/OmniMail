from fastapi import FastAPI
from app.routers import emails


app = FastAPI()

@app.get("/")
def read_root():
    return {"Message":"hello World"}

app.include_router(emails.router,prefix="/email",tags=["Email endpoints"])