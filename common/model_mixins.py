from django.utils.timezone import now
from django.db import models


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def is_soft_deleted(self):
        return self.deleted_at is not None

    def soft_delete(self):
        self.deleted_at = now()
        self.save()
