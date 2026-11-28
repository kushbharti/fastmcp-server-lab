import jwt
import uvicorn
from datetime import timedelta,datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

from config import setting

app = FastAPI(title="JWT Token Generator")

class TokenRequest(BaseModel):
    user_id:str
    email:str
    password:str
    
class TokenResponse(BaseModel):
    access_token:str
    expire_in:int


@app.post("/token",response_model=TokenResponse)
def generate_token(req:TokenRequest):
    now = datetime.now(timezone.utc)
    exp = now + timedelta(hours=setting.JWT_EXPIRE_HOURS)
    
    payload = {
        "sub": req.user_id,
        "email": req.email,
        "iat": now,
        "exp":exp,
        "iss":setting.JWT_ISSUER,
        "aud":setting.JWT_AUDIENCE
    }
    token = jwt.encode(payload, setting.JWT_SECRET, algorithm=setting.JWT_ALGORITHM)
    return TokenResponse(access_token=token, expire_in=setting.JWT_EXPIRE_HOURS)


@app.get('/')
def health():
    return {
        "status": "OK"
    }
    
if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8001)