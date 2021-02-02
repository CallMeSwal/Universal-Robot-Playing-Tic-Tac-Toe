# Echo client program
import socket
import time
HOST = "192.168.1.5"    # The remote host
PORT = 30002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
hi=int(input("PROMPT"))
s.send("set_digital_out(6,True)" + "\n")
time.sleep(2)
s.send("set_digital_out(3,True)" + "\n")
time.sleep(2)
s.send("set_digital_out(1,True)" + "\n")
time.sleep(2)
s.send("set_digital_out(2,True)" + "\n")
time.sleep(2)
data = s.recv(1024)
s.close()
print("Received", repr(data))

