"""
making a server
"""

import socket

s = socket.socket()
s.bind(("0.0.0.0", 8080))
s.listen(10)

http_resp = b"""HTTP/1.1 200 OK\r
Content-Length: 10\r


hi there\n\r
"""

conn, add = s.accept()
print(conn.recv(4096))
conn.send(http_resp)
conn.shutdown(socket.SHUT_RDWR)
conn.close()
s.close()
