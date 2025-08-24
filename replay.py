import socket
PAYLOAD = """474554202f706572666f726d2f25324120485454502f312e310d0a486f73743a203132372e302e302e313a383030300d0a557365722d4167656e743a204d6f7a696c6c612f352e3020285831313b205562756e74753b204c696e7578207838365f36343b2072763a3134312e3029204765636b6f2f32303130303130312046697265666f782f3134312e300d0a4163636570743a206170706c69636174696f6e2f6a736f6e0d0a4163636570742d4c616e67756167653a20656e2d55532c656e3b713d302e350d0a4163636570742d456e636f64696e673a20677a69702c206465666c6174652c2062722c207a7374640d0a526566657265723a20687474703a2f2f3132372e302e302e313a383030302f646f63730d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a5365632d46657463682d446573743a20656d7074790d0a5365632d46657463682d4d6f64653a20636f72730d0a5365632d46657463682d536974653a2073616d652d6f726967696e0d0a5072696f726974793a20753d300d0a0d0a"""

TARGET_IP = "127.0.0.1"
PORT = 8000

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
    
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting")
    s.connect((TARGET_IP,PORT))
    print("Connected")
    print("Sending payload")
    s.send(bytearray.fromhex(PAYLOAD))
    print(get_parsed_response(s))
    s.close()
except:
    print("Failed")
else:
    print("Sent")
    


