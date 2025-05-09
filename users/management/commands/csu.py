from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя."""

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@email.com"
        if not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username, email=email)
            user.set_password("admin")
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
