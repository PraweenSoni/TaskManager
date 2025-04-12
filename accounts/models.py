from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class NormalUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # for email verification
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
