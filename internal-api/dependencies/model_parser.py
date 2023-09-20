from dependencies.models.participant import Participant
import logging
from datetime import datetime
DATA_ROOT = {"deltager": "Vrdeltagerperson"}


def parse(endpoint, data: dict):
    rows = []
    try:

        root = DATA_ROOT.get(endpoint)

        # for record in data:
        #     d = record["_source"][root]['naermesteFremtidigeDato']
        #     logging.info(d)
        records = [Participant(**{**record["_source"][root], "_id": record["_id"]}) for record in data]
        rows = [record.dict() for record in records if not record.cvr_id is None]
    except Exception as e:
        logging.error(f"parse failed with {e}")

    return rows
