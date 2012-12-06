from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
from catfactsmsgqueue import createmsgqueue as cmq
# Create your models here.

class Recipient(models.Model):
    number = PhoneNumberField(unique=True)

    def __unicode__(self):
        return self.number
   
    def start_catfacts(self):
        cmq.queue_msg_tasks_for_new_user('+1' + ''.join(self.number.split('-')))
        print 'catfacts started for: ' + self.number