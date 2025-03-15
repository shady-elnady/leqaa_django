from django.forms import ModelForm

from Category.models import Category


class CategoryAdminForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "image",
            "translations",
        ]
