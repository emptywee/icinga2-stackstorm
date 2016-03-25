from lib.client import Client
import sys

class Icinga2Action():

    def __init__(self, api_url, api_user, api_password, method):
        self.body = ''
        self.error = 0
        self.api_url = api_url
        self.api_user = api_user
        self.api_password = api_password
        self.method = method

    def run(self):
        pass
      
    def get_client(self):
        client = Client(self, self.api_url, self.api_user, self.api_password, self.method)
        return client

    def get_error(self):
        return self.error
    
    def get_body(self):
        #sys.stderr.write(str(self.body))
        return self.body

    def set_body(self, body):
        #sys.stderr.write('setting body')
        self.body = body
        