from django.forms import ModelForm
from django.contrib.admin.widgets import AdminFileWidget

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Firebase.widgets import FirebaseImageWidget

from Category.models import Category


class CategoryAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize widgets here if needed, e.g., for the image field
        # self.fields["image"].widget = forms.FileInput()
        pass

    class Meta:
        model = Category
        fields = [
            "name",
            "image",
            # "firebase_image_url",
            "translations",
        ]
        widgets = {
            "firebase_image_url": FirebaseImageWidget(),
            "image": AdminFileWidget(),  # Regular widget for the flag field
            "translations": MyTranslationWidget,
        }
