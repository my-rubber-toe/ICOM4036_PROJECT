import logging
import sys
import socketserver
import uuid
import socket


from dao.echo_server import EchoServer, EchoRequestHandler
from dao.echo_client import EchoClient

nev = {}

def message_server(server):

    server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    message = input("Your message: ")
    sock.sendall(bytes(message,'ascii'))
    response = str(sock.recv(1024), 'ascii')
    print("Received: {}".format(response))
    sock.close()


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # let the kernel assign a port automatically
    server = EchoServer(address)
    server2 = EchoServer(address)
    client = EchoClient()
    

    server.run_me()
    client.send_message("hello", server)





