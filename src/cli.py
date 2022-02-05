import typer
from typing import Optional

import config
from adapters.security_score_api_adapter import SecurityScoreApiAdapter

__app_name__ = "security-score-cli"
__version__ = "0.1.0"


app = typer.Typer()

security_score_api_client = SecurityScoreApiAdapter(api_url=config.API_URL,api_port=config.API_PORT)

@app.command()
def scan_trending_repos(access_token: str = typer.Option(...,"--access-token","-t", \
    help="Access token in ghp format, see: https://docs.github.com/en/authentication/ \
        keeping-your-account-and-data-secure/creating-a-personal-access-token"), \
        count:int= typer.Option(...,"--cout","-c", help="number of reposiroties to scan")):
    repos_data = security_score_api_client.get_trending_repos_secure_score(access_token=access_token,count=count)
    print(repos_data)

@app.command()
def version():
    typer.echo(f"My superCLI Version: {__version__}")

@app.callback()
def callback():
    """
    Code security measurement CLI tool.

    Wait for future versions and alot more insights 
    """
