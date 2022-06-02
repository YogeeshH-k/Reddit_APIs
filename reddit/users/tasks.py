from django.core.mail import send_mail


def send_forgot_username_mail(username, recipient_email):
    subject = "So you wanna know your Reddit username, huh?"
    message = f"Hi there,\n You forgot it didn't you? \nHey, it happens. Here you go:\n Your username is {username}\n" \
              f"(Username checks out, nicely done.)"
    send_mail(subject=subject, message=message, from_email=None, recipient_list=[recipient_email], fail_silently=True)
    return True
