import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.189.142",80))
s.sendall(b"POST /~handsome/testpost.php HTTP/1.1\r\n")
content="username=123"
content_Length= f"Content-Length:{str(len(content))}\r\n\r\n"
s.sendall(b"Host: 192.168.189.142\r\n")
s.sendall(b"Connection: keep-alive\r\n")
s.sendall(b"Content-Type: application/x-www-form-urlencoded\r\n")
s.sendall(content_Length.encode("utf-8"))
s.sendall((content+"\r\n").encode("utf-8"))
data=s.recv(1024)
s.close()
print('Received', data.decode('utf-8'))