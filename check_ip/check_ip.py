import sys

import typer
from httpx import Client, codes, Response

from method import Method


app = typer.Typer()


def send_request(method: str, url: str, params: dict = {}):
    with Client() as client:
        response: Response = client.request(method, url, **params)

        return response.json(), response.status_code


@app.command("Check IP address")
def main(ip: str = typer.Option(..., "--ip", "-i", help="IP address to check")):
    url = f"http://ip-api.com/json/{ip}"
    error_msg = {"msg": "Invalid IP address."}

    data, status = send_request(Method.get.value, url)

    sys.stdout.write(str(data))
    return data if status == codes.OK else error_msg


if __name__ == "__main__":
    app()
