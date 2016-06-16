import time, json, re, os
from datetime import datetime
from slackclient import SlackClient
#token = 'xoxb-50784128320-QUEE4BbBCPYhliQPYhOcY0Vr'
token = int(os.environ.get('slack_api_key'))
sc = SlackClient(token)

chan = 'D1GP6ABCM'

def post(msg):
    sc.api_call('chat.postMessage', as_user='true:', channel=chan, text=msg)

recv_msg =''

def checkmsg(recv_msg):
    if recv_msg.lower() == 'hello':
        post('Greetings')
    elif ' time ' in recv_msg.lower():
        post(str(datetime.now()))

if sc.rtm_connect():
    post('JDBOT ON THE JOB')
    while True:
      new_evts = sc.rtm_read()
      for evt in new_evts:
          if "type" in evt:
              if evt["type"] == "message" and "text" in evt:
                  message=evt["text"]
                  print message
                  checkmsg(message)
                  time.sleep(3)
else:
    print "Connection Failed."



#greeting = 'Hello!\nNice to meet you.'

#print sc.api_call('api.test')
#print sc.api_call('im.open', user='U0F9CDVUP')

#print sc.api_call('chat.postMessage', as_user='true:', channel=chan, text=greeting)
#print sc.api_call('im.history', channel=chan)
