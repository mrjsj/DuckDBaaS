import logging
from dependencies import cvr_functions as cvr
from dependencies import db_functions as db
from dependencies import model_parser as mp
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psutil

# from dependencies.model_parser import parse

app = FastAPI()

ENDPOINT_TRANSLATOR = {
    "deltager": "participants",
    "virksomhed": "companies",
    "produktionsenhed": "productionunits",
}


@app.get("/load")
def load_data(endpoint: str):
    if not endpoint in ENDPOINT_TRANSLATOR.keys():
        raise ValueError("Wrong endpoint!")

    try:
        timestamp = db.get_latest_timestamp(endpoint)
        data = cvr.cvr_request(endpoint, timestamp)
        parsed_data = mp.parse(endpoint, data)
        db.write(ENDPOINT_TRANSLATOR.get(endpoint), parsed_data)
        return {"message": f"inserted {len(parsed_data)} to {endpoint}"}
    except Exception as e:
        return {"message": f"Function failed with error {e}"}


if __name__ == "__main__":
    load_data("deltager")


@app.get("/")
async def root():
    # Call the functions to get the information

    # Get the information
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_space = get_disk_space()
    linux_distro = get_linux_distro()

    # Create an HTML report
    report = f"""
    <html>
    <head>
        <title>System Information Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #333333;
            }}
            pre {{
                background-color: #f6f8fa;
                padding: 10px;
                overflow: auto;
            }}
        </style>
    </head>
    <body>
        <h1>System Information Report</h1>
        <h2>CPU Information:</h2>
        <pre>{cpu_info}</pre>
        <h2>Memory Information:</h2>
        <pre>{memory_info}</pre>
        <h2>Disk Space Information:</h2>
        <pre>{disk_space}</pre>
        <h2>Linux Distribution Information:</h2>
        <pre>{linux_distro}</pre>
    </body>
    </html>
    """
    return HTMLResponse(content=report, status_code=200)


import subprocess


def get_cpu_info():
    command = "cat /proc/cpuinfo"
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    if error:
        print("Error retrieving CPU information:", error.decode())
    else:
        return output.decode()


def get_memory_info():
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024**3), 2)
    used = round(memory.used / (1024**3), 2)
    free = round(memory.available / (1024**3), 2)
    return f"Total: {total} GB, Used: {used} GB, Free: {free} GB"


def get_disk_space():
    command = "df -h"
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    if error:
        print("Error retrieving disk space information:", error.decode())
    else:
        return output.decode()


def get_linux_distro():
    command = "cat /etc/os-release"
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    if error:
        print("Error retrieving Linux distribution information:", error.decode())
    else:
        return output.decode()
