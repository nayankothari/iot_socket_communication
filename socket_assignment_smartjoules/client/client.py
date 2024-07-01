"""
We use this code to create a client side connection and send
necessary command to server for execution and waiting for response from server.
we use uuid to generate unique id on every  request.
"""

import socket
import json
import uuid


class Client:
    """
    Creating Client class to send commands to server.
    """

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, host_ip, port):
        self.client_socket.connect((host_ip, port))
        
    def request(self, request_obj):
        request_data = json.dumps(request_obj).encode('utf-8')
        self.client_socket.sendall(request_data)
        
        response_data = self.client_socket.recv(4096).decode('utf-8')
        response_obj = json.loads(response_data)
        
        return response_obj


if __name__ == '__main__':
    """
    Bottle neck execution of client module.
    """

    client = Client()
    # IP as per our server public IP address.
    client.connect('localhost', 9999)

    # Can send commands or need to change path id run on server.
    request_object = [
        {
            'method': 'mkdir D:\\nayan\\iot-hackthon\\test_folder',
            'id': str(uuid.uuid4())
        },
        {
            'method': 'mkdir D:\\nayan\\iot-hackthon\\test_folder2',
            'id': str(uuid.uuid4())
        }
    ]
    
    response = client.request(request_object)
    print(response)
    # If we need to implement any business logic based on the response we can write from here.
