from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.aboutus.models import ResumeApplication , Vacancy
from apps.common.models.model import Feedback , Application
from apps.main.models import NewsletterEmail

from apps.main.tasks import (
    send_application_task,
    send_feedback_task,
    send_vacancy_task,
    send_resume_task
)

from django.contrib.auth.models import User

import environ
env = environ.Env()
env.read_env(".env")


# @receiver(post_save , sender=News)


@receiver(post_save , sender=Feedback)
def send_feedback(sender , instance , **kwargs):
    print("feedback signal ishladi")
    subject = instance.full_name
    id = instance.id
    phone_number = str(instance.phone_number)
    email = instance.email
    message = instance.message
    from_email = env.str("EMAIL_HOST_USER")
    recipient_list = [user.email for user in User.objects.filter(is_staff=True)]
    send_feedback_task.delay(subject , id , phone_number , email , message , from_email , recipient_list)




@receiver(post_save , sender=Application)
def send_application(sender , instance , **kwargs):
    print("application signal ishladi")
    subject = instance.full_name
    id = instance.id
    phone_number = str(instance.phone_number)
    message = instance.question
    from_email = env.str("EMAIL_HOST_USER")
    recipient_list = [user.email  for user in  User.objects.all()]
    send_application_task.delay(subject , id , phone_number ,message ,from_email , recipient_list)





@receiver(post_save , sender=Vacancy)
def send_vacancy(sender , instance , **kwargs):
    if instance.active:
        subject = instance.title_ru
        message = instance.description_ru
        slug = instance.slug
        from_email = env.str("EMAIL_HOST_USER")
        recipient_list = [user.email for user in User.objects.all()]
        send_vacancy_task.delay(subject , message , slug , from_email , recipient_list)






@receiver(post_save, sender=ResumeApplication)
def send_resume(sender, instance, **kwargs):
    subject = instance.full_name
    id = instance.id
    phone_number = str(instance.phone_number)
    from_email = env.str("EMAIL_HOST_USER")
    recipient_list = [user.email for user in User.objects.all()]
    send_resume_task.delay(subject, id, phone_number, from_email, recipient_list)


