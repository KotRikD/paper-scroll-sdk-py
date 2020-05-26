from . import client, methods


class PaperScroll:

    def __init__(self, merchant_id: int, access_token: str):
        self.access_token = access_token
        self.merchant_id = merchant_id

        self.client = client.PaperScrollClient(access_token, merchant_id)
        self.api = methods.PaperScrollMethods(self.client)
    
    def getApi(self):
        return self.api
    
    def getClient(self):
        return self.client
