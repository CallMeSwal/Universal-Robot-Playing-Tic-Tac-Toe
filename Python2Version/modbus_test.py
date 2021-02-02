# Echo client program
import socket
import time
HOST = "192.168.1.5"    # The remote host
PORT = 30002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
hi=int(input("PROMPT"))
s.send("modbus_set_output_register('MODBUS_1', 4, False)" + "\n")
time.sleep(2)
s.send("modbus_set_output_register('MODBUS_3', 4, False)" + "\n")
time.sleep(2)
s.send("modbus_set_output_signal('MODBUS_2', True, False)" + "\n")
time.sleep(2)
s.send("set_digital_out(2,True)" + "\n")
time.sleep(2)
data = s.recv(1024)
s.close()
print("Received", repr(data))

