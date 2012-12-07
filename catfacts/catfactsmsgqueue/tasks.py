from celery import task
from twilio.rest import TwilioRestClient
import datetime

@task(name='catfactsmsgque.sendsms.send_sms')
def send_sms(sms_to, sms_from, sms_body):
	client = TwilioRestClient()
	message = client.sms.messages.create(
									to=sms_to, 
									from_=sms_from,
									body=sms_body
									)
	return True