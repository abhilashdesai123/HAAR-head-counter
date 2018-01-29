from twilio.rest import TwilioRestClient
file = open("testfile.txt", "r") 
count=file.read()
accountSid ="Put your twilio account SID here"
authToken ="Put your twilio account authToken here"
twilioClient =TwilioRestClient(accountSid, authToken)
myTwilioNumber ="Put your twilio number here"
destCellPhone ="Put your registered recipient number here"
myMessage = twilioClient.messages.create(body ="Crowd Count is "+count, from_=myTwilioNumber, to=destCellPhone)
print("Crowd count: "+count)

