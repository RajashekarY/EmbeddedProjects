import requests
import json
import datetime
URL = 'https://www.way2sms.com/api/v1/sendCampaign'

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
response = sendPostRequest(URL, '06S00GGWBJK6OQTAUEH7TMXCNU0B50TK', 'U44RMESW4B44NBIW', 'stage', '8686563675', 'active-sender-id', 'Training Halted at {}'.format(datetime.datetime.now()) )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)