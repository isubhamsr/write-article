from django.db import models

# Create your models here.
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_title = models.CharField(max_length=255)
    document_description = models.TextField()
    document = models.FileField(upload_to='document/files')
    number_of_words = models.IntegerField()
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_id} - {self.document_title}"