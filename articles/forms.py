from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "is_published"]
        labels = {
            "title": "標題",
            "content": "內文",
            "is_published": "是否發布",
        }
        widgets = {
            "title": TextInput(attrs={"class": "input"}),
            "content": Textarea(attrs={"class": "textarea", "rows": 5,}),
            "is_published": CheckboxInput(attrs={"class": "checkbox"}),
        }
