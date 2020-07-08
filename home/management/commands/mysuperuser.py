import os
import secrets
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='claxtastic').exists():
            User.objects.create_superuser('claxtastic', 'claxtons4@gmail.com', secrets.POSTGRES_PASSWORD)
