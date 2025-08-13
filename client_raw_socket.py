#!/usr/bin/env python
import socket
import urllib.parse


HOST = "127.0.0.1"
PORT = 8000
BASIC_URL = "http://127.0.0.1:8000/"
OPERATIONS_LIST = ["+", "-",  "*", "\\", "u", "r", "c"]

def generate_init_req(number):
    request = (
        f"GET /initial?number={number} HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Connection: keep-alive\r\n"
        "\r\n"
    )
    return request
def generate_perform_req(operation):
    
    if operation in OPERATIONS_LIST:
        operation = urllib.parse.quote(operation)
    request = (
        f"GET /perform/{operation} HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Connection: keep-alive\r\n"
        "\r\n"
    )
    return request

def reconnect():
    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_sock.connect((HOST, PORT))
    return new_sock

def get_parsed_response(sock):
    response = b""
    while b"\r\n\r\n" not in response:
        part = sock.recv(1024)
        if not part:
            break
        response += part

    headers, part2, body = response.partition(b"\r\n\r\n") # part 2 = b"\r\n\r\n"
    headers = headers.decode()
    
    content_length = 0
    for header in headers.split("\r\n"):
        if header.lower().startswith("content-length:"):
            content_length = int(header.split(":")[1].strip())
            break

    while len(body) < content_length:
        part = sock.recv(1024)
        if not part:
            break
        body += part
    print("Response: ", body)
    return body
def is_valid_operation(operation):
    if operation in OPERATIONS_LIST and len(operation) == 1:
        return True
    else:
        return False
        
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address_and_port = (HOST, PORT)
    sock.connect((HOST, PORT))
    
    number = input("Enter initial number: ")
    sock.send(generate_init_req(number).encode())
    response = get_parsed_response(sock)
 
    operation = input("Enter operation( + - * \\ u c r e): ")
    while operation != "e":
        if is_valid_operation(operation):
            try:
                sock.send(generate_perform_req(operation).encode())
            except BrokenPipeError:
                print("Reconnect... the socket was broken")
                sock.close()
                sock = reconnect()
                continue 
            response = get_parsed_response(sock).decode()
            
            response = response.split(":")[1].split("}")[0]
            
            print("current number: ", response)
        else:
            print("invalid operation")
        operation = input("Enter operation( + - * \\ u c r e): ")
        


if __name__ == "__main__":
    main()







