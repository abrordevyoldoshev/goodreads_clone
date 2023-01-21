from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import CustomUser


# Bu admin tarafdan user qoshsa ishlaydi faqat buni apps.py da import qilib qoyish kerak

# qachon ishlashligini bildirish uchun bu code @receiver()
@receiver(post_save, sender=CustomUser)
def send_welcome_emil(sender, instance, created, **kwargs):
    # <= send email code buni settengisga kirib nastroyka qilish kerak =>
    if created:
        send_mail(
            "Welcome to goodreads clone",
            f" Hi, {instance.username} Welcome to Goodreads Clone. Enjoy the books end review.",
            'frontend47@gmail.com',
            [instance.email],
        )
