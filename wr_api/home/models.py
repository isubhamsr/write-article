from django.db import models

# Create your models here.
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_title = models.CharField(max_length=255)
    document_description = models.TextField()
    document = models.FileField(upload_to='document/files', blank=True)
    number_of_words = models.IntegerField()
    customar_email = models.EmailField(default="")
    deadline_date = models.CharField(max_length=255, default="")
    deadline_time = models.CharField(max_length=255, default="")
    work_price = models.CharField(max_length=255, default="")
    pages = models.IntegerField(default=0)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_id} - {self.document_title}"