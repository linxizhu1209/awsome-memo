from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id: str
    content: str


memos = []

app = FastAPI()

@app.get("/memos")
def read_memo():
    return memos

@app.post("/memo")
def create_memo(memo:Memo):
    memos.append(memo)
    return "메모 성공"




app.mount("/mem", StaticFiles(directory="static",html=True), name="static")



