import typer
from typing import Optional

__app_name__ = "security-score-cli"
__version__ = "0.1.0"


app = typer.Typer()

@app.command()
def set_access_token():
    print("hi")

