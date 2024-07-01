"""
We are using this standalone server file for creation of socket server and
execution of client commands.
we import socket and threading library to achieve the desired result.

Python -v 3.7, socket -v 3.3
"""

import json
import socket
import subprocess
from threading import Thread


class Server:
    """
    We use class Server to start the execution process on server to serve multiple requests in a threads.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Here we are starting our execution process.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5) # 5 we use for maximum queue size
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")

            # Handle client request in a new thread or process
            # For simplicity, we handle each client sequentially
            client_thread = Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        """
        Handling requests here.
        """
        request_data = client_socket.recv(4096).decode('utf-8')

        try:
            request_objs = json.loads(request_data)

            if isinstance(request_objs, list):
                response_objs = []

                for request_obj in request_objs:
                    response_obj = self.process_single_request(request_obj)
                    response_objs.append(response_obj)

                response_data = json.dumps(response_objs).encode('utf-8')
                client_socket.sendall(response_data)
            else:
                response_obj = self.process_single_request(request_objs)
                response_data = json.dumps(response_obj).encode('utf-8')
                client_socket.sendall(response_data)

        except json.JSONDecodeError:
            response_obj = {
                'error_code': 1
            }
            response_data = json.dumps(response_obj).encode('utf-8')
            client_socket.sendall(response_data)
        except Exception as e:
            print(f"Internal server error: {e.__str__()}")
            response_obj = {
                'error_code': 4
            }
            response_data = json.dumps(response_obj).encode('utf-8')
            client_socket.sendall(response_data)

        # Finally here are closing the connection.
        client_socket.close()

    def process_single_request(self, request_obj):
        method = request_obj.get('method')
        request_id = request_obj.get('id')
        print(method, "this is the command.")
        if method:
            result = self.execute_command(method)
            response_obj = {
                'result': result['returncode'],
                'stdout': result['stdout'],
                'stderr': result['stderr'],
                'id': request_id,
                'error_code': 0
            }
        else:
            response_obj = {
                'error_code': 2
            }

        return response_obj

    def execute_command(self, command):
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result)
        return {
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr
        }


if __name__ == '__main__':
    # Here we can change IP address as per our server public IP.
    server = Server('localhost', 9999)
    server.start()
