import logging
import os
from datetime import date, datetime

from dotenv import load_dotenv
from fastapi import FastAPI
from models.participant import Participant
from utils.sample_data import DELTAGER

from supabase import Client, create_client
from utils.cvr_queries import get_should
import requests

load_dotenv()

# Set up logger
logging.basicConfig(filename="./app/app.log", encoding="utf-8", level=logging.DEBUG)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


deltagere = DELTAGER["hits"]["hits"]

participants = [
    Participant(**deltager["_source"]["Vrdeltagerperson"]) for deltager in deltagere
]

partitipants_data = [participant.dict() for participant in participants]

import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


# print(participants)

# with open("data/participants.json", "w") as file:
#     json.dump(partitipants_data, file, indent=4, cls=CustomJSONEncoder)


app = FastAPI()


# @app.get("/get_participants")
def participant():
    data = [
        {
            "business_key": "1",
            "position": "cio",
        },
        {
            "business_key": "2",
            "position": "ceo",
        },
    ]
    try:
        supabase.table("participants").upsert(
            data, on_conflict="business_key"
        ).execute()
    except Exception as e:
        logging.error(e)
        return {"status": "error"}
    logging.info("success")
    return {"status": "success"}


def get_latest_timestamp(endpoint: str) -> datetime:
    response = (
        supabase.table("meta_last_loaded")
        .select("datetime_value")
        .eq("endpoint", endpoint)
        .single()
        .execute()
    )

    timestamp = datetime.strftime(
        datetime.fromisoformat(response.data["datetime_value"]), "%Y-%m-%dT%H:%M:%S"
    )
    return timestamp


def cvr_request(endpoint: str, timestamp: str) -> dict:
    LIMIT = 20
    url = f"http://distribution.virk.dk/cvr-permanent/{endpoint}/_search?scroll=1m"
    headers = {"Content-Type": "application/json"}
    should = get_should(endpoint, timestamp)
    query = {"query": {"bool": {"should": should}}, "size": LIMIT}

    auth = (os.environ.get("CVR_USER"), os.environ.get("CVR_PASSWORD"))
    initial_response = requests.get(url, json=query, headers=headers, auth=auth)

    if not initial_response.status_code == 200:
        logging.warning(initial_response.headers)
        return
    
    data = initial_response.json()["hits"]["hits"]
    length = len(data)

    scroll_id = initial_response.json()["_scroll_id"]

    while length >= LIMIT:
        url = f"http://distribution.virk.dk/_search/scroll"
        query = {"scroll_id": f"{scroll_id}", "scroll": "1m"}
        response = requests.get(url, json=query, headers=headers, auth=auth)

        if not response.status_code == 200:
            logging.warning(initial_response.headers)
            return
        
        scroll_id = response.json()["_scroll_id"]

        tmp_data = response.json()["hits"]["hits"]
        length = len(tmp_data)
        data += tmp_data

    return data


print(cvr_request("deltager", "2023-06-01"))
