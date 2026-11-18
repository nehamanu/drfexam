
from django.db.models.signals import pre_save
from employee.models import Employee
from django.dispatch import receiver



@receiver(pre_save, sender=Employee)
def show_message(sender, instance, **kwargs):
    instance.name = instance.name.capitalize()
