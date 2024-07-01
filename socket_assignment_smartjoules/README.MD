# Socket programming for assignment of smart joules.

Dear Dishant / Akshit,

This project implements a communication channel between a client and server using socket 
programming in Python. It allows the client to execute 
OS commands on the server and receive responses.


### Instructions for uses

```markdown
To send a requests to the server by client:

from client import Client

client = Client()
client.connect('localhost', 9999)

request_object = {
    "method": "mkdir D:\\nayan\\iot-hackthon\\test_folder",
    "id": "123456789-123456-123456-123456789"
}

response = client.request(request_object)
print(response)

```
### Code Structure and Design

```markdown

The is structured into two main modules:

- `client.py`: Contains the Client class for interacting with the server.
- `server.py`: Implements the Server class to handle incoming client requests.
```

### Design Principles

```markdown
- Followed Oops principles in both modules.
- Followed SOLID principles to ensure modularity and maintainability.
```

## Contact

For questions or support, 
please contact Nayan kothari (mailto:nayankothari1997@gmail.com).
