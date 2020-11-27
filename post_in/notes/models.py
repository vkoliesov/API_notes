from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id = {self.pk}, title = {self.title}"

    class Meta:
        ordering = ['-updated']