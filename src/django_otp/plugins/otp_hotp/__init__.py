import django


if django.VERSION < (3, 2):
    default_app_config = 'django_otp.plugins.otp_hotp.apps.DefaultConfig'
