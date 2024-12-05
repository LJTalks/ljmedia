from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    featured_image = CloudinaryField(
        'image', null=True, blank=True, default='placeholder'
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Alt text for the image"
    )
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    website_url = models.URLField(
        max_length=500, blank=True, help_text="URL of the live website")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Dynamically set the alt text if not provided
        if not self.alt_text:
            self.alt_text = f"Image of {self.title}"
        super().save(*args, **kwargs)
