
from dao.echo_server import EchoServer
from dao.echo_client import EchoClient
import requests

import logging

logging.basicConfig(filename= "env_logs.log",level=logging.DEBUG,format='%(name)s: %(message)s',)

class EnvController:
    """Object to control the language environment"""
    def __init__(self):
        self.logger = logging.getLogger('EnvController')
        self.env = dict()
    
    
    def create_server(self, server_name, ip, port):
        """Set new server to the environment"""
        address = (ip, port)
        if(not (server_name in self.env)):
            new_server = EchoServer(address)
            new_server.run_me()
            self.env[server_name] = new_server
            return
    
        self.env.__delitem__(server_name)
        self.env[server_name] = EchoServer(address).run_me()
    
    def create_client(self,client_name):
        """Set a new client to the environment."""
        self.env[client_name] = EchoClient()
    
    def delete_object(self, object_name):
        """Remove Object from environment"""
        return self.env.popitem(object_name)
    
    def var_assign(self, var_name, value):
        if(not isinstance(value,(str, int))):
            print(f'Unassigned variable: value must be integer or string')
            return
        
        self.env[var_name] = value    

    def send_message(self, var1, var2, message):
        if(not self.env[var1]):
            print(f'Error: Unasigned variable {var1}=None')
            return
        if(not self.env[var2]):
            print(f'Error: Unasigned variable {var2}=None')
            return

        if(isinstance(self.env[var1], EchoClient)  and isinstance(self.env[var2], EchoServer)):
            client : EchoClient = self.env[var1]
            server : EchoServer = self.env[var2]
            client.send_message(message, server)

        elif(isinstance(self.env[var1], EchoServer)  and isinstance(self.env[var2], EchoServer)):
            s1 : EchoServer = self.env[var1]
            s2 : EchoServer = self.env[var2]
            s1.message_peer(message, s2)

    def info(self, var_name):
        try:
            x = self.env[var_name]
            if(isinstance(x,(str, int))):
                print(x)
            elif(isinstance(x,(EchoClient, EchoServer))):
                print(x)

        except Exception:
            print(f'Unassigned variablle: variable \"{var_name}\" is not assigned')
    
    def connect_external(self, var):
        var_value = self.verify_var(var)
        if(not var_value): # If there is not a variable
            self.logger.debug(f'connecting to {var}')
            req = requests.get(url=var)
            print(f'Response from {var}: {req.status_code}')
        else:
            self.logger.debug(f'connecting to {var_value}')
            req = requests.get(url=var_value)
            print(f'Response from {var_value}: {req.status_code}')


    def verify_var(self, var):
        try:
            return self.env[var]
        except KeyError:
            return None
                
    def __repr__(self):
        return self.env
        
