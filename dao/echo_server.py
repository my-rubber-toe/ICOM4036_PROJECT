import logging
import sys
import socketserver
import uuid
import socket
import threading

logging.basicConfig(filename= "env_logs.log",level=logging.DEBUG,format='%(name)s: %(message)s',)


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.sendall(data)
        
        return
    
class EchoServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    
    def __init__(self, server_address:tuple):
        # socketserver.TCPServer.__init__(self, server_address, handler_class)

        super().__init__(server_address, EchoRequestHandler)
        self.server_id = uuid.uuid4()
        self.logger = logging.getLogger(f'EchoServer({self.server_id})')
        self.logger.debug(f'server created ip={self.server_address[0]} port={self.server_address[1]}')
        self.is_running = False
    
    def finish_request(self, request, client_address):
        print(f'Server handled request from {client_address}')
        self.logger.debug(f'request handled')
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

    def message_peer(self, message, peer):
        """Send message to a peer server"""
        try:
            self.logger.debug(f'sending message to peer={peer.server_id}, message={message}')
            ip, port = peer.server_address
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(bytes(message,'ascii'))
            print(f'Server({self.server_id}): {message}')
            response = str(sock.recv(1024), 'ascii')
            sock.close()
            self.logger.debug(f'recieved response from peer={peer.server_id}, response={response}')
        except:
            print(f'Unable to send message to {peer}')

    def __repr__(self):
        ip, port = self.server_address
        return f'EchoServer<server_id={self.server_id}, ip={ip}, port={port}>'