from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "published", "slug", "image")
        widgets = {
            "body": CKEditor5Widget(config_name="default"),
            "slug": forms.TextInput(attrs={
                'placeholder': 'برای مثال: hello-world123، hello_world123 (بدون فاصله، کاراکتر خاص یا ایموجی)'
            }),
        }

