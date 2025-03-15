from fastapi import FastAPI
from app.api.v1.endpoints import analytics, notes, summarize
from app.database.base import Base
from app.database.session import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(summarize.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes Management System"}