from datetime import datetime, timedelta

from jose import jwt

from data_service.auth.models import Token
from settings import settings


def create_access_token(personaname: str) -> Token:
    expires_delta = timedelta(minutes=30)
    expires_at = datetime.utcnow() + expires_delta

    token_payload = {
        "sub": personaname,
        "exp": expires_at,
    }

    access_token = jwt.encode(
        token_payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )

    return Token(access_token=access_token, token_type="bearer")
