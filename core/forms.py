from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False
    
    class Meta:
        model = Post
        fields = ("img","title","body","Category")
        
        # widgets = {
        #       "body": CKEditor5Widget(
        #           attrs={"class": "django_ckeditor_5"}, config_name="extends"
        #       )
        #   }
        content = CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends")
        
        
        
        
        
        

