import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_ADMIN_USERNAME")
password = os.environ.get("DJANGO_ADMIN_PASSWORD")

if not username or not password:
    print("Admin credentials not configured.")
elif User.objects.filter(username=username).exists():
    print(f"User '{username}' already exists.")
else:
    User.objects.create_superuser(
        username=username,
        email="",
        password=password,
    )
    print(f"Superuser '{username}' created successfully.")