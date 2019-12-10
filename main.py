import logging
import sys
import socketserver
import uuid
import socket


from dao.echo_server import EchoServer, EchoRequestHandler
from dao.echo_client import EchoClient

env = {}

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # let the kernel assign a port automatically
    # create server myserver ip port
    server = EchoServer(address)
    server.run_me()

    env[server] = server
    client = EchoClient()
    client.send_message("Hello", env[server])

    server.stop_me()







