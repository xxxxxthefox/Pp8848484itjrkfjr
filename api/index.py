
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys, io, contextlib

app = FastAPI()

class CodeReq(BaseModel):
    user: str
    code: str
    key: str

@app.get("/api/status")
def status():
    return {"status": "Fox Engine Online"}

@app.post("/api/execute")
async def execute(data: CodeReq):
    if data.key != "FOX_SECRET_2026":
        raise HTTPException(status_code=401, detail="Unauthorized")
    f = io.StringIO()
    try:
        with contextlib.redirect_stdout(f):
            exec(data.code)
        return {"output": f.getvalue()}
    except Exception as e:
        return {"output": str(e)}
