from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True, default=None)
    is_approve_user = models.BooleanField(default=False)
    details = models.TextField(blank=True, null=True, default=None)
    remark = models.TextField(blank=True, null=True, default=None)
    created_user = models.TextField(blank=True, null=True, default=None)
    updated_user = models.TextField(blank=True, null=True, default=None)
    deleted_user = models.TextField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(blank=True, null=True, default=None)
    updated_at = models.DateTimeField(blank=True, null=True, default=None)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table: str = "roles"
