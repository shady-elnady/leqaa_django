# from django.db.models import ForeignKey, PROTECT
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseImageModel
from Locale.models.BaseTranslationModel import BaseTranslationModel

# Create your mofrom django.utils.text import slugify


class Category(BaseTranslationModel, BaseImageModel):
    # category_parent = ForeignKey(
    #     "self",
    #     null=True,
    #     blank=True,
    #     limit_choices_to={"category_parent__isnull": True},
    #     on_delete=PROTECT,
    #     related_name="Sub_Categories",
    #     verbose_name=_("Category Parent"),
    # )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
