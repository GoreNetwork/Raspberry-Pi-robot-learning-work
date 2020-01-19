from gpiozero import LED
import time
import time
import slack
import requests
token = 'xoxp-887994720226-887995702098-902608463013-0d7fdb41963ed2a63445b00d290721ab'

channel = 'CSGP7NMMK'
file_name='blink_speed.txt'

def get_last_message(token, channel):
	url = 'https://slack.com/api/conversations.history?token={}&channel={}&limit=1&pretty=1'.format(token, channel)
	r = requests.get(url)
	all_response = r.json()
	#print (all_response)
	last_message = all_response['messages'][0]['text']
	return last_message

def to_doc_w(file_name, varable):
	f=open(file_name, 'w')
	f.write(varable)
	f.close()

while True==True:
	to_doc_w(file_name,get_last_message(token, channel))
	time.sleep(2)
