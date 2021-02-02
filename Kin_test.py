# Echo client program
import socket
import time
HOST = "192.168.1.5"    # The remote host
PORT = 30002              # The same port as used by the server
print("Starting Program")
count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(0.05)
s.send("set_digital_out(2,True)" + "\n")
time.sleep(0.1)
print("0.2 seconds are up already")
s.send("set_digital_out(7,True)" + "\n")
time.sleep(2)
s.send("movej([-0.5405182705025187, -2.350330184112267, -1.316631037266588, -2.2775736604458237, 3.3528323423665642, -1.2291967454894914], a=1.3962634015954636, v=1.0471975511965976)" + "\n")
time.sleep(2)
s.send("movej([-0.7203210737806529, -1.82796919039503, -1.8248107684866093, -1.3401161163439792, 3.214294414832996, -0.2722986670990757], a=1.3962634015954636, v=1.0471975511965976)" + "\n")
time.sleep(2)
print("0.2 seconds are up already")
s.send("set_digital_out(7,False)" + "\n")
time.sleep(1)
count = count + 1
print("The count is:", count)
time.sleep(1)
data = s.recv(1024)
s.close()
print("Received", repr(data))
print("Program finish")
