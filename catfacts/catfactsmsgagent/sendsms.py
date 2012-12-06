from celery import Celery
from twilio.rest import TwilioRestClient
import datetime

celery = Celery('tasks', backend='amqp', broker='django://')

@celery.task(name='CatfactsMsgAgent.sendsms.send_sms')
def send_sms(sms_to, sms_from, sms_body):
	client = TwilioRestClient()
	message = client.sms.messages.create(
									to=sms_to, 
									from_=sms_from,
									body=sms_body
									)
    print "----------> *** CATFACT MSG EXEXCUTED"

	return True