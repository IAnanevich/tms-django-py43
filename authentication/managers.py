from django.conf import settings
from django.contrib.auth.models import UserManager as BaseUserManager
from django.core.mail import send_mail  # send_mass_mail


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        response = super().create_user(username, email, password, **extra_fields)
        send_mail(
            subject='Test',
            message='Activate',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        # message_1 = (
        #     'Test',
        #     'Activate',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email, ],
        # )
        # message_2 = (
        #     'Test 2',
        #     'Activate 2',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email, ],
        # )
        # send_mass_mail((message_1, message_2))

        return response
