import requests
import json
import datetime
URL = 'https://www.way2sms.com/api/v1/sendCampaign'
# Send SMS using python and Way2SMS
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'your-API-Key-Here', 'your-Password', 'stage', 'Receivers-Number', 'active-sender-id', 'Training Halted at {}'.format(datetime.datetime.now()) )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)