import json
import os

file_path = os.path.dirname(__file__)

with open(f"{file_path}\\deltager.json") as f:
    DELTAGER = json.load(f)

with open(f"{file_path}\\produktionsenhed.json") as f:
    PRODUKTIONSENHED = json.load(f)

with open(f"{file_path}\\virksomhed.json") as f:
    VIRKSOMHED = json.load(f)
