from django.db import models

class RevokedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    is_explicit = models.BooleanField(default=False)

    def __str__(self):
        return self.token