#!/usr/bin/env python
from st2actions.runners.pythonrunner import Action
from lib.client import Client
from lib.icinga2action import Icinga2Action

import sys,urllib

class Icinga2GetHost(Action):
        
    def run(self, hosts):
        api_suffix = ''
        if hosts:
            if len(hosts) == 1:
                api_suffix = '?host=' + urllib.quote_plus(hosts[0])
            else:
                api_suffix += '?'
                for host in hosts[:-1]:
                    api_suffix += 'hosts=' + urllib.quote_plus(host) + '&'
                api_suffix += 'hosts=' + urllib.quote_plus(hosts[-1])
            
        self.logger.debug('URL suffix: %s', api_suffix)
        self.api_url = self.config['api_url'] + '/objects/hosts' + str(api_suffix)
        self.api_user = self.config['api_user']
        self.api_password = self.config['api_password']
        self.method = 'get'
        self.logger.debug('Action Icinga2GetHost started')
        ia = Icinga2Action(self.api_url, self.api_user, self.api_password, self.method)
        client = ia.get_client()
        client.make_call()
        if ia.get_error() == 0:
            return ia.get_body()
        else:
            sys.exit(ia.get_error())
    
