from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.core.mail import send_mail

# Отправка уведомления администратору о том, что товар закончился
@receiver(post_save, sender=Product)
def send_email_on_zero_quantity(sender, instance, **kwargs):
    if instance.quantity == 0:
        send_mail(
            subject=f"Товар {instance.title} закончился на складе!",
            message=f"Срочно попольните склад, товар {instance.title} закончился на складе.",
            from_email='your_email@example.com',
            recipient_list=['admin_email@example.com'],
            fail_silently=False
        )