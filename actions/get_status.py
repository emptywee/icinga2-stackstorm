#!/usr/bin/env python
from st2actions.runners.pythonrunner import Action
from lib.client import Client
from lib.icinga2action import Icinga2Action
import sys

class Icinga2GetStatus(Action):
        
    def run(self):
        self.api_url = self.config['api_url'] + '/status'
        self.api_user = self.config['api_user']
        self.api_password = self.config['api_password']
        self.method = 'get'
        self.logger.debug('Action Icinga2GetStatus started')
        ia = Icinga2Action(self.api_url, self.api_user, self.api_password, self.method)
        client = ia.get_client()
        client.make_call()
        if ia.get_error() == 0:
            return ia.get_body()
        else:
            sys.exit(1)
    
