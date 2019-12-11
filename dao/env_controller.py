
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
        """Set new server to the environment. If port = 0, then kernel will take care of the port"""
        the_ip = ip
        the_port =port

        var_ip = self.verify_var(ip)

        if(var_ip):
            the_ip = var_ip

        try:
            if(port == 0): print(f'Random port will be assigned.')
            address = (the_ip, the_port)
            new_server = EchoServer(address)
            new_server.run_me()
            self.env[server_name] = new_server
        except Exception as e:
            if(isinstance(e, TypeError)):
                print(f'ERROR: Unrecognized variable.')
            if(isinstance(e, OSError)):
                print(f'ERROR: {e}.')
            
    
    def create_client(self,client_name):
        """Set or update client to the environment."""
        if(self.verify_var(client_name)):
            print(f'ERROR: client with the name \"{client_name}\" already exists.')
            return
        self.env[client_name] = EchoClient()
    
    def delete_client_or_server(self, var_name):
        """Remove server or client from environment"""
        value = self.verify_var(var_name)
        if(isinstance(value, EchoServer)):
            value.stop_me()
            removed_server = self.env.pop(var_name)
            self.logger.debug(f'server removed server_id={removed_server.server_id}')
            return removed_server
        elif(isinstance(value, EchoClient)):
            removed_client = self.env.pop(var_name)
            self.logger.debug(f'client removed client_id={removed_client.client_id}')
            return removed_client
        elif(isinstance(value, (int, str))):
            print(f'ERROR: Variable {var_name} is not of type: \"EchoServer\" or \"EchoClient\" ')
        else:
            print(f'ERROR: Unrecognized variable \"{var_name}\"')
    
    def var_assign(self, var_name, value):
        if(not isinstance(value,(str, int))):
            print(f'Unassigned variable: value must be integer or string')
            return
        
        self.env[var_name] = value    

    def send_message(self, sender, receiver, message):
        the_sender = self.verify_var(sender)
        the_receiver = self.verify_var(receiver)
        if(not the_sender):
            print(f'Error: Unasigned variable {sender}=None')
            return
        if(not the_receiver):
            print(f'Error: Unasigned variable {receiver}=None')
            return
    
        if(isinstance(the_sender, EchoClient)  and isinstance(the_receiver, EchoServer)):
            client : EchoClient = the_sender
            server : EchoServer = the_receiver
            client.send_message(message, server)

        elif(isinstance(the_sender, EchoServer)  and isinstance(the_receiver, EchoServer)):
            s1 : EchoServer = the_sender
            s2 : EchoServer = the_receiver
            s1.message_peer(message, s2)

    def info(self, var_name):
        something = self.verify_var(var_name)
        if(something):
            print(something)
        else:
            print(f'ERROR: Unrecognized variable: {var_name}')
    
    def connect_external(self, sender, external_address):

        the_sender = self.verify_var(sender)
        the_external_address = external_address

        tmp_var = self.verify_var(external_address)
        if(isinstance(tmp_var, str)):
            the_external_address = tmp_var
            
        if(isinstance(the_sender, (EchoClient, EchoServer))):
            the_sender.send_external(external_address)
        else:
            print(f'ERROR: Variable is not type \"EchoServer\" or \"EchoClient\"')


    def verify_var(self, var):
        try:
            return self.env[var]
        except KeyError:
            return None
                
    def __repr__(self):
        return self.env
        
