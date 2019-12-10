import logging
import uuid
from dao.echo_server import EchoServer
import socket


logging.basicConfig(filename= "server_logs.log",level=logging.DEBUG,format='%(name)s: %(message)s',)


class EchoClient:
    def __init__(self):
        self.client_id = uuid.uuid4()
        self.logger = logging.getLogger(f'Client({self.client_id})')
        self.connections = dict()

        self.logger.debug('client created')
    
    def info(self):
        return self.__repr__()
        
    def add_local_connection(self, server: EchoServer):
        self.connections.__setitem__(server, server)

    def add_external_connection(self, address: tuple):
        pass

    def send_message(self, message, server: EchoServer):
        ip, port = server.server_address
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.sendall(bytes(message,'ascii'))
        print(f'Client({self.client_id}): {message}')

        response = str(sock.recv(1024), 'ascii')
        sock.close()
        self.logger.debug(f'Successfully sent message to server={server.server_id}')
        return True

        



    def close_connection(self, server: EchoServer):
        return self.connections.popitem(server)
    
    
    def __repr__(self):
        return f'Client<client_id={self.client_id}, connections={self.connections}>'

