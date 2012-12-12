import datetime

from tasks import send_sms
from factlistgenerator import generate_cat_facts_message_sequence


SENDING_NUMBER = "+17694473276"

def queue_msg_tasks_for_new_user(recipient_number):
    catfact_message_sequence = generate_cat_facts_message_sequence()

    for message_index, catfact_message in enumerate(catfact_message_sequence):
        delay_amount = 9*message_index # send a message every 9 hours (because cats have 9 lives!) Meow!
        time = datetime.datetime.utcnow() + datetime.timedelta(hours=delay_amount)
        send_sms.apply_async((recipient_number, SENDING_NUMBER, catfact_message), eta=time)
        print recipient_number, SENDING_NUMBER, catfact_message, time
