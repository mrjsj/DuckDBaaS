from supabase import create_client
from os import getenv
from datetime import datetime
import logging
import json
supabase_url = getenv("SUPABASE_URL", "")
supabase_key = getenv("SUPABASE_KEY", "")
supabase = create_client(supabase_url, supabase_key)

UNIQUE_KEYS = {
    "participants": "cvr_id",
    "companies": "xxx",
    "productionunit": "xxx",
}


def get_latest_timestamp(endpoint: str) -> datetime:
    try:
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
    except Exception as e:
        logging.error(f"get_latest_timestamp failed with {e}")

    return timestamp


def write(table, data):
    unique_key = UNIQUE_KEYS.get(table)

    if unique_key is None:
        raise ValueError(f"{table} is not a valid endpoint.")

    try:
        supabase.table(table).upsert(json.loads(json.dumps(data, default=str)), on_conflict=unique_key).execute()
    except Exception as e:
        logging.error(e)
        return {"status": "error"}
    logging.info("success")
    return {"status": "success"}
