from django import forms
from home.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_title', 'document_description', 'document', 'number_of_words',
                    'customar_email', 'deadline_date', 'deadline_time', 'work_price', 'pages')