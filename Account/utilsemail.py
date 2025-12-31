from django.core.mail import send_mail
from django.conf import settings

def Email_send(user_email,username,role,name,password):
  send_mail(
    subject="Completion Of Registrations",
    message=f"""
Hy {name} Role is {role}
User Id:{username}
Password:{password}

Congratulation Your Account Created Successfully

Please Loging and Update Carefully

Please Change Your Password For Security

Regards,
Team

""",
from_email=settings.EMAIL_HOST_USER,
recipient_list=[user_email],
fail_silently=False,
  )