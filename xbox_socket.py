import inputs
import socket
import time


print(inputs.devices.gamepads)
import martypy


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#get on local host IP, on port 1234
s.bind(('192.168.0.89', 1234))

s.listen(5)

#while True:
#	#clinetsocket= Client socket object 
#	#address = client's address
#	clientsocket, address = s.accept()
#	print (f' Connection from {address} has been established!!')
#	clientsocket.send(bytes("welcome to the server",'utf-8'))


pads = inputs.devices.gamepads


if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")
	
big_number=0	
#while True:
clientsocket, address = s.accept()
print (f' Connection from {address} has been established!!')
#clientsocket.send(bytes("welcome to the server",'utf-8'))

while True:
	events = inputs.get_gamepad()
	for event in events:
		lstick_x=0
		if event.code=="ABS_X":
			lstick_x=event.state
			lstick_x = lstick_x/32767
			lstick_x=lstick_x*90+90
			print ("Lstick L/R",lstick_x)
			time.sleep(.1)
			if lstick_x<0:
				lstick_x=0
			clientsocket.send(bytes(str(lstick_x),'utf-8'))



#Absolute ABS_X 2693