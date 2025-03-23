from typing import List


class Resource:
    def __init__(self, url: str, project_id: str,):
        self.url = url
        self.project_id = project_id
        self.endpoints = []

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)
