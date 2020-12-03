from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id = {self.pk}, title = {self.title}"

    class Meta:
        ordering = ['-updated']