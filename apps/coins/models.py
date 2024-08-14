from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class GeekCoin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_update = models.DateTimeField(default=now)

    def add_coins(self, amount):
        self.balance += amount
        self.last_update = now()
        self.save()

    def check_and_burn_coins(self):
        today = now()
        last_month = today.replace(day=1) - timedelta(days=1)
        last_month_start = last_month.replace(day=1)
        
        if self.last_update < last_month_start:
            self.balance = 0
            self.save()

@receiver(post_save, sender=GeekCoin)
def burn_coins_if_needed(sender, instance, **kwargs):
    instance.check_and_burn_coins()






class Transaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_transactions', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
