import datetime

from celery import task
from twilio.rest import TwilioRestClient


@task(name='catfactsmsgque.sendsms.send_sms')
def send_sms(recipient_number, sending_number, sms_body):
    client = TwilioRestClient()
    message = client.sms.messages.create(
                                    to=recipient_number, 
                                    from_=sending_number,
                                    body=sms_body
                                    )
    return True
