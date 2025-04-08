from celery import shared_task
from django.core.mail import send_mail
from smtplib import SMTPRecipientsRefused
from apps.main.models import *
from apps.main.helpers import InstagramScraper
from apps.common.models.model import Contact
from django.core.files.uploadedfile import SimpleUploadedFile
from core.celery import app

import environ
env = environ.Env()
env.read_env(".env")



# @shared_task
# def send_newsletter_task(subject ,message , img_url , slug , from_email ,recipient_list):
#     post_url = "http://127.0.0.1:8000/" + slug
#     my_message = f"""
#     <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
#         <img src="https://admin.wayu.uz/static/img/wayu-login.png">
#         <h1 style="font-size: 40px !important; width: 80% !important;">{subject}</h1>
#         <div style="display: flex; justify-content: flex-end;">
#         <img src={img_url} style="width: 80% !important;">
#         </div>
#         <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">{message}</p>
#         <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
#         <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
#        </p>
#     </div>
#     """

#     for recipient in recipient_list:
#         try:
#             send_mail(
#               subject=subject,
#               message=message,
#               html_message=my_message,
#               from_email=from_email,
#               recipient_list=(recipient , ),
#             )
#         except SMTPRecipientsRefused:
#             NewsletterEmail.objects.get(email=recipient).delete()
    


@shared_task
def send_feedback_task(subject , id , phone_number , email ,message,from_email , recipient_list):
    post_url = f"http://127.0.0.1:8000/admin/common/feedback/{id}"
    my_message = f"""
        <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
            <h1 style="font-size: 40px !important; width: 80% !important;">Feedback for WAYU</h1>
            <div style="display: flex; justify-content: flex-end;">
            </div>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Full name: {subject}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Phone number: {phone_number}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Email: {email}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">{message}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
            <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
           </p> 
        </div>
        """
    
    for recipient in recipient_list:
        print("feedback task ishladi")
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=my_message,
                from_email=from_email,
                recipient_list=(recipient,),
            )
        except SMTPRecipientsRefused:
            pass



@shared_task
def send_application_task(subject, id, phone_number, message, from_email, recipient_list):
    post_url = "http://127.0.0.1:8000/admin/common/application/" + str(id)
    print(f"Generated URL: {post_url}") 
    my_message = f"""
        <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
            <h1 style="font-size: 40px !important; width: 80% !important;">Application for WAYU</h1>
            <div style="display: flex; justify-content: flex-end;">
            </div>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Full name: {subject}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Phone number: {phone_number}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">{message}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
            <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
           </p>
        </div>
        """

    for recipient in recipient_list:
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=my_message,
                from_email=from_email,
                recipient_list=(recipient,),
            )
        except SMTPRecipientsRefused:
            pass


# @shared_task
# def send_feedback_project_task(subject, id, email, project, message, from_email, recipient_list):
#     post_url = "http://127.0.0.1:8000/admin/projects/feedbackprojects/" + str(id)
#     my_message = f"""
#         <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
#             <h1 style="font-size: 40px !important; width: 80% !important;">Feedback for {project}</h1>
#             <div style="display: flex; justify-content: flex-end;">
#             </div>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Project: {project}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Full name: {subject}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Email: {email}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">{message}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
#             <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
#            </p>
#         </div>
#         """

#     for recipient in recipient_list:
#         try:
#             send_mail(
#                 subject=subject,
#                 message=None,
#                 html_message=my_message,
#                 from_email=from_email,
#                 recipient_list=(recipient,),
#             )
#         except SMTPRecipientsRefused:
#             pass


# @shared_task
# def send_volunteer_resume_task(subject, id, phone_number, email, from_email, recipient_list):
#     post_url = "http://127.0.0.1:8000/admin/services/volunteerresume/" + str(id)
#     my_message = f"""
#         <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
#             <h1 style="font-size: 40px !important; width: 80% !important;">Resume for volunteer</h1>
#             <div style="display: flex; justify-content: flex-end;">
#             </div>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Full name: {subject}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Phone number: {phone_number}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Email: {email}</p>
#             <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
#             <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
#            </p>
#         </div>
#         """

#     for recipient in recipient_list:
#         try:
#             send_mail(
#                 subject=subject,
#                 message=None,
#                 html_message=my_message,
#                 from_email=from_email,
#                 recipient_list=(recipient,),
#             )
#         except SMTPRecipientsRefused:
#             pass


@shared_task
def send_vacancy_task(subject, message, slug, from_email, recipient_list):
    post_url = "http://127.0.0.1:8000/admin/aboutus/GetSingleVacancy/" + slug
    print(f"Generated URL: {post_url}") 
    my_message = f"""
    <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
        <img src="https://admin.wayu.uz/static/img/6428227673.jpg">
        <h1 style="font-size: 40px !important; width: 80% !important;">{subject}</h1>
        <div style="display: flex; justify-content: flex-end;">
        </div>
        <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">{message}</p>
        <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
        <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
       </p>
    </div>
    """

    for recipient in recipient_list:
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=my_message,
                from_email=from_email,
                recipient_list=(recipient,),
            )
        except SMTPRecipientsRefused:
            pass


@shared_task
def send_resume_task(subject, id, phone_number, from_email, recipient_list):
    post_url = "http://127.0.0.1:8000/admin/aboutus/resumeapplication/" + str(id)
    my_message = f"""
        <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
            <h1 style="font-size: 40px !important; width: 80% !important;">Resume</h1>
            <div style="display: flex; justify-content: flex-end;">
            </div>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Full name: {subject}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Phone number: {phone_number}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
            <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
           </p>
        </div>
        """

    for recipient in recipient_list:
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=my_message,
                from_email=from_email,
                recipient_list=(recipient,),
            )
        except SMTPRecipientsRefused:
            pass


@app.task()
def scrape_instagram():
    MyInstagramScraper = InstagramScraper(env.str("INSTAGRAM_USERNAME") , env.str("INSTAGRAM_PASSWORD"))
    MyInstagramScraper.scrape(Contact.objects.first().instagram)
    for i in MyInstagramScraper.images:
        image = SimpleUploadedFile(name="test_image.jpg",content=open(i[0], "rb").read() , content_type="image/jpeg")
        if not InstagramPhoto.objects.filter(link=i[1]).exists():
            InstagramPhoto.objects.create(img=image , link=i[1])

