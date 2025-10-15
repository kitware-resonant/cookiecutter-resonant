from hashlib import sha512

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from s3_file_field import S3FileField


class Image(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    blob = S3FileField()
    checksum = models.CharField(max_length=128, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # TimeStampedModel also provides "created" and "modified" fields

    @property
    def short_checksum(self) -> str | None:
        return f'{self.checksum[:10]}' if self.checksum else None

    def compute_checksum(self) -> None:
        hasher = sha512()
        with self.blob.open() as blob:
            for chunk in blob.chunks():
                hasher.update(chunk)
        self.checksum = hasher.hexdigest()
