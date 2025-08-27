import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.full_name or str(self.id)


class Place(models.Model):
    PLACE_TYPES = [
        ("centre_de_sante", "Centre de santé"),
        ("clinique", "Clinique"),
        ("pharmacie", "Pharmacie"),
        ("boutique_hygiene", "Boutique Hygiène"),
        ("association", "Association"),
        ("orphelinat", "Orphelinat"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    place_type = models.CharField(max_length=50, choices=PLACE_TYPES)
    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    hours = models.CharField(max_length=255, blank=True)
    specialties = models.CharField(max_length=255, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey('denniba.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='places')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.get_place_type_display()})"


class Vocal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded_by = models.ForeignKey('denniba.User', on_delete=models.CASCADE, related_name='vocals')
    file = models.FileField(upload_to='vocals/%Y/%m/%d/')
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vocal {self.id} by {self.uploaded_by}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey('denniba.User', on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=280)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    audio = models.ForeignKey(Vocal, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post {self.id} by {self.author}"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('denniba.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment {self.id} on {self.post.id}"
