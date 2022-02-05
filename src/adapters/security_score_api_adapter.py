import typing
import json

import requests
class SecurityScoreApiAdapter:
    def __init__(self, api_url,api_port):
        self.service_endpoint = f"{api_url}:{str(api_port)}"
    
    def get_trending_repos_secure_score(self, access_token: str,count: int):
            endpoint_url = f'{self.service_endpoint}/v1/repos/trending'
            params = {'access_token':access_token, "count":count}
            response = requests.get(endpoint_url, params=params)
            response.raise_for_status()
            return response.json()
            
        