###
# We want to do incremental loads based on column `sidstOpdateret`
# Below function can help us

from sample_data import DELTAGER, PRODUKTIONSENHED, VIRKSOMHED
from datetime import datetime

TARGET_KEY = "sidstOpdateret"
DATE = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
IGNORE_PATH = ["hits", "hits", 0, "_source"]


def find_paths_with_key(
    json_obj: dict, target_key, current_path="", unique_paths=set()
):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == target_key:
                unique_paths.add(current_path + "." + key)
            elif isinstance(value, (dict, list)):
                if current_path:
                    new_path = f"{current_path}.{key}"
                else:
                    new_path = key
                find_paths_with_key(value, target_key, new_path, unique_paths)
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_path = f"{current_path}"
            find_paths_with_key(item, target_key, new_path, unique_paths)
    return list(unique_paths)


def should_builder(data: dict):
    for node in IGNORE_PATH:
        data = data[node]
    paths = find_paths_with_key(data, TARGET_KEY)

    return [{"range": {f"{path}": {"gte": f"{DATE}"}}} for path in paths]


def elastic_search_query_builder():
    data = PRODUKTIONSENHED
    should = should_builder(data)
    query = {"query": {"bool": {"should": should}}, "size": 2500}
    return should


print(elastic_search_query_builder())
