from dao.echo_server import EchoServer, EchoRequestHandler
from dao.echo_client import EchoClient
from dao.env_controller import EnvController

import requests

env = {}

if __name__ == '__main__':

    env_ctrl = EnvController()

    # env_ctrl.create_server("server1", "localhost", 0)
    # env_ctrl.create_server("server2", "localhost", 0)
    # env_ctrl.send_message("server1", "server2", "hi")
    # env_ctrl.var_assign("external", "http://www.google.com")
    # env_ctrl.info("new_var")
    # env_ctrl.info("server1")
    env_ctrl.connect_external("http://www.google.com")










