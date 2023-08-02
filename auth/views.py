from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from auth.jwt import create_access_token
from database.session import get_session
from steam.openid import STEAM_OPENID_URL, STEAM_OPENID_AUTH_PARAMS, is_valid
from steam.webapi.endpoints import get_player_summaries
import users.service as user_service

router = APIRouter()


@router.get("/login")
async def login():
    return RedirectResponse(url=f'{STEAM_OPENID_URL}?{STEAM_OPENID_AUTH_PARAMS}',
                            status_code=303)


@router.get("/login/callback")
async def login_callback(request: Request, db_session: Session = Depends(get_session)):
    query_params = request.query_params
    ok = is_valid(dict(query_params))

    if not ok:
        raise HTTPException(status_code=401, detail="Not Authenticated")

    user_steamid = dict(query_params)['openid.claimed_id'].split('/')[-1]  # get steamid in validated request
    user = user_service.get(db_session=db_session, steamid=user_steamid)
    if not user:
        print(f"[INFO]: creating account for user with steamid: {user_steamid}")
        user_data = get_player_summaries([user_steamid])["response"]["players"][0]
        user_service.create(db_session=db_session, user_in=user_data)

    access_token = create_access_token(user.personaname)
    return access_token


@router.get("/logout")
async def logout():
    pass
