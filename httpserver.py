import socket
import json
import threading 
from requests.auth import HTTPBasicAuth 
import sys

class HttpServer:
  
    def __init__(self):
        pass
    def listen(self,data,port):
        self.port = port
        self.proto = "HTTP/1.1 200 OK"
        headers = {
            "Content-Length": len(data)*2, #len(data)*2 / sys.getsizeof(data)
            "content-type": "text/html; charset=UTF-8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,da;q=0.8,ru;q=0.7",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        serversocket = socket.socket()
        self.data = data
        hostname = socket.gethostname()
        dns_resolved_addr = socket.gethostbyname(hostname)
        try:
            serversocket.bind((dns_resolved_addr, self.port)) #self.port
        except socket.error as msg:
            print("Bind failed.\n{}".format(msg))
        print("Listening on {}:{}".format(socket.gethostbyname(socket.gethostname()), self.port)) 
        serversocket.listen()
        while True:
            client, (conn, addr) = serversocket.accept()
            while True:
                print("[+] {}:{} has connected".format(conn,addr)) # conn is the ip, addr is the port
                print("Sending required HTTP headers and data..") 
                client.send(self.proto.encode())
                client.send("\n".encode())
                for i in headers:
                    client.send(i.encode())
                client.send("\n".encode())
                client.send(self.data.encode())
                break
def main():
    try:
        file = sys.argv[1]
        port = int(sys.argv[2])
        HttpServer().listen(open(file).read(),port)
    except Exception as msg:
        print("Syntax: python -m httpserver htmlfile port")
        sys.exit()
if __name__ == "__main__":
    main()
