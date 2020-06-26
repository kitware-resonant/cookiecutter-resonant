from hashlib import sha512
from typing import Optional

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Image(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    blob = models.FileField()
    checksum = models.CharField(max_length=128, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # TimeStampedModel also provides "created" and "modified" fields

    @property
    def short_checksum(self) -> Optional[str]:
        return f'{self.checksum[:10]}' if self.checksum else None

    def compute_checksum(self) -> str:
        hasher = sha512()
        with self.blob.open() as blob:
            for chunk in blob.chunks():
                hasher.update(chunk)
        return hasher.hexdigest()
