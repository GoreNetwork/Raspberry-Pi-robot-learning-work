import inputs

print(inputs.devices.gamepads)
import martypy



pads = inputs.devices.gamepads


if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")
	
big_number=0	
while True:
	events = inputs.get_gamepad()
	for event in events:
		#print(event.ev_type, event.code, event.state)
		if event.code=="ABS_RZ":
			acc=event.state/255
			acc=acc*100
			print ('acc',acc)
		if event.code=="ABS_Z":
			brk=event.state/255
			brk=brk*100
			print ('break',brk)
		if event.code=="ABS_Y":
			lstick_y=event.state
			lstick_y = lstick_y/32767
			lstick_y=lstick_y*100
			if abs(lstick_y) < 10:
				lstick_y=0
			print ("l stick-up/down",lstick_y)
		if event.code=="ABS_X":
			lstick_x=event.state
			lstick_x = lstick_x/32767
			lstick_x=lstick_x*100
			if abs(lstick_x) < 10:
				lstick_x=0
			print ("Lstick L/R",lstick_x)

#Absolute ABS_X 2693