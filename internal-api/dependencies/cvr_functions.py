from dependencies.templates.elastic_search_template import get_should
from os import getenv
import logging
import requests


def cvr_request(endpoint: str, timestamp: str) -> dict:
    try:
        LIMIT = 20
        url = f"http://distribution.virk.dk/cvr-permanent/{endpoint}/_search?scroll=1m"
        headers = {"Content-Type": "application/json"}
        should = get_should(endpoint, timestamp)
        query = {"query": {"bool": {"should": should}}, "size": LIMIT}

        auth = (getenv("CVR_USER", ""), getenv("CVR_PASSWORD", ""))
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

    except Exception as e:
        logging.error(f"cvr_request failed with {e}")

    return data
