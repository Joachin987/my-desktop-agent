import requests
import json

class SearchTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.googleapis.com/customsearch/v1'

    def search(self, query, **kwargs):
        params = {
            'key': self.api_key,
            'q': query,
        }
        params.update(kwargs)
        response = requests.get(self.base_url, params=params)
        return response.json()