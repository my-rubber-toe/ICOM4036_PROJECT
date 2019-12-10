import logging
import sys
import socketserver
import uuid
import socket
import threading


logging.basicConfig(filename= "server_logs.log",level=logging.DEBUG,format='%(name)s: %(message)s',)

class EchoRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.sendall(data)
        print(data)
        return
    
class EchoServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    
    def __init__(self, server_address):
        # socketserver.TCPServer.__init__(self, server_address, handler_class)

        super().__init__(server_address, EchoRequestHandler)
        self.server_id = uuid.uuid4()
        self.logger = logging.getLogger(f'EchoServer({self.server_id})')
        self.logger.debug(f'server created ip={self.server_address[0]} port={self.server_address[1]}')
        self.is_running = False
    
    def finish_request(self, request, client_address):
        
        return super().finish_request(request, client_address)
    
    def run_me(self):
        """Run server to handle each request on a diferent thread."""
        t = threading.Thread(target=self.serve_forever)
        t.daemon = True  # don't hang on exit
        t.start()
        self.is_running = True
    
    def stop_me(self):
        self.logger.debug('closing server')
        self.shutdown()
        self.server_close()
    
    def connect_peer(self, peer):
        """Establish a connection with a peer server"""
        pass

    def message_peer(self):
        """Send message to a peer server"""
        pass

    def __repr__(self):
        ip, port = self.server_address
        return f'EchoServer<server_id={self.server_id}, ip={ip}, port={port}>'