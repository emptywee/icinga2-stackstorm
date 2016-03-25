#!/usr/bin/env python
from st2actions.runners.pythonrunner import Action
from lib.client import Client
from lib.icinga2action import Icinga2Action

import sys,urllib

class Icinga2GetService(Action):
        
    def run(self, services):
        api_suffix = ''
        if services:
            if len(services) == 1:
                api_suffix = '?service=' + urllib.quote_plus(services[0])
            else:
                api_suffix += '?'
                for service in services[:-1]:
                    api_suffix += 'services=' + urllib.quote_plus(service) + '&'
                api_suffix += 'services=' + urllib.quote_plus(services[-1])
            
        self.logger.debug('URL suffix: %s', api_suffix)
        self.api_url = self.config['api_url'] + '/objects/services' + str(api_suffix)
        self.api_user = self.config['api_user']
        self.api_password = self.config['api_password']
        self.method = 'get'
        self.logger.debug('Action Icinga2GetService started')
        ia = Icinga2Action(self.api_url, self.api_user, self.api_password, self.method)
        client = ia.get_client()
        client.make_call()
        if ia.get_error() == 0:
            return ia.get_body()
        else:
            sys.exit(ia.get_error())
    
