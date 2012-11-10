from sendsms import send_sms
from catfactgen import generate_cat_facts
import datetime

FromNum = "+1XXXXXXXXXX"
ToNum = "+1XXXXXXXXXX"

list = generate_cat_facts()
list = ['Welcome to CatFacts! The coolest Way to learn about cats! Your first CatFact: Cats spend a third of their waking hours grooming themselves!'] + list

for index, msg in enumerate(list):
	delayAmount = index
	time = datetime.datetime.utcnow() + datetime.timedelta(minutes=delayAmount)
	send_sms.apply_async((ToNum, FromNum, msg), eta=time)
