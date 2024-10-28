#Question 1: By default are django signals executed synchronously or asynchronously? 
Ans. - By default, Django signals are executed synchronously. When a signal is sent, the receiver 
       functions are executed immediately within the same request-response cycle.


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading
from django.db import transaction
from django.db import models



@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, created, **kwargs):
    print("Signal received!")
    time.sleep(5)  
    print("Signal processing completed.")

user = User.objects.create(username="test_user")

print("User created!")





#Question 2: Do Django signals run in the same thread as the caller?
Ans. - Yes, by default, Django signals run in the same thread as the caller. The signal handler is 
       executed in the same thread as the main execution.

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, created, **kwargs):
    print("Signal running in thread:", threading.current_thread().name)

user = User.objects.create(username="test_user")
print("Main thread:", threading.current_thread().name)  




#Question 3: Do Django signals run in the same database transaction as the caller?
Ans. - Yes, Django signals run in the same database transaction as the caller, meaning if 
       the transaction is rolled back, any changes made in the signal handler will also be rolled back.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created within transaction")


try:
    with transaction.atomic():
        user = User.objects.create(username="transaction_user")
        raise Exception("Forcing rollback!")
except:
    print("Transaction rolled back, no profile created.")

print(Profile.objects.filter(user__username="transaction_user").exists())        