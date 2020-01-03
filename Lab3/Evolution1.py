import nexmo
from flask import Flask, render_template, requet

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
'''
client1= nexmo.Client(key = '5edb949f', secret = 'HmmoGd4Qhc1u4COc')

number = input('Enter the phone number:')
message = input('Enter the message: ')

response = client1.send_message({'from': '18146674515', 'to': number,'text': message })

response = response['message'][0]

if response['status'] == '0':
	print ('Send message ', response['message-id'])
else:
	print ('Error ', response['error-text'])
'''

if __name__ == '__main__':
	app.run(debug=True)
