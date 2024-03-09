import jwt
from datetime import datetime, timedelta
from pathlib import Path
from fastapi.security import HTTPBearer,  HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, Depends, status



class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not await self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    async def verify_jwt(self, jwt_token: str):
        is_token_valid = False

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("http://users_fastapi:8000/auth/validate", json={"token": jwt_token})
            is_token_valid = True
        except jwt.ExpiredSignatureError:
            is_token_valid = False
        except jwt.InvalidTokenError:
            is_token_valid = False
        return is_token_valid