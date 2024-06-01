from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    # For use purpose, all field must be filled
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=200, blank=False)
    text_description = models.TextField(blank=False)
    text_explication = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True, unique=True)    # Will be used for the view
    phone = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    # published_date = models.DateTimeField(blank=True, null=True)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()
#

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.id)
            self.save()

    def __str__(self):
        return self.title
