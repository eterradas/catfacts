from sendsms import send_sms
from factlistgenerator import generate_cat_facts_message_sequence
import datetime


def queue_msg_tasks_for_new_user(ToNum):
    FromNum = "+17694473276"

    catlist = generate_cat_facts_message_sequence()
    catlist=catlist[0:2]

    for index, msg in enumerate(catlist):
        delayAmount = 9*index # send a message every 9 hours (because cats have 9 lives!) Meow!
        time = datetime.datetime.utcnow() + datetime.timedelta(hours=delayAmount)
        send_sms.apply_async((ToNum, FromNum, msg), eta=time)
        print ToNum, FromNum, msg, time
