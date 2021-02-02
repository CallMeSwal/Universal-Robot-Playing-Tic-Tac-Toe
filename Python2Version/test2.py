# Echo client program
import socket
import time
HOST = "192.168.1.5"    # The remote host
PORT = 30002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
hi=int(input("PROMPT"))
s.send("sec set_digital_out(3,True)" + "\n")
time.sleep(0.25)
data = s.recv(1024)
s.close()
print("Received", repr(data))

