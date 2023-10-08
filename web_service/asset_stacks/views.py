from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from db_service. import Depot
import db_service.accounts.service as accounts_service
import db_service.asset_stacks.service as asset_stacks_service
from api_service.steam.communityapi.endpoints import SteamCommunityEndpoints
from db_service.session import get_session
from web_service.asset_stacks.models import Depot

router = APIRouter()


@router.get("/get/")
async def get_inventory(steamid: str, db_session: Session = Depends(get_session)):
    print(steamid)
    if not accounts_service.exists(db_session=db_session, steamid=steamid):
        print("no account existing")
        accounts_service.create(db_session=db_session, account_in={"steamid": steamid})
        SteamCommunityEndpoints.fetch_inventory(db_session=db_session, steamid=steamid)
    result = asset_stacks_service.get_asset_count_for_each_stack(db_session=db_session, steamid=steamid)
    asset_stacks = {"asset_stacks": [r._asdict() for r in result]}

    return Depot(**asset_stacks)
