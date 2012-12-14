from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

from catfacts.apps.catfactsmsgqueue.createmsgqueue import queue_msg_tasks_for_new_user

class Recipient(models.Model):
    number = PhoneNumberField(unique=True)

    def __unicode__(self):
        return self.number
   
    def start_catfacts(self):
        queue_msg_tasks_for_new_user('+1' + ''.join(self.number.split('-')))
        print 'catfacts started for: ' + self.number