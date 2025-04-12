from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField,
    CharField,
)
from django.utils.translation import get_language, to_locale

from Category.models import Category


# class TranslatedNameField(CharField):
#     def to_representation(self, value):
#         request = self.context.get("request")
#         if request:
#             try:
#                 current_language = to_locale(get_language())
#                 if value and isinstance(value, dict) and current_language in value:
#                     return value.get(current_language)
#                 elif value:
#                     # Fallback to the default name if translation is not found
#                     return value
#                 else:
#                     return ""
#             except AttributeError:
#                 pass  # Handle cases where request might not be available
#         return value  # Return the original name if no request or language info


class BaseTranslationSerializer(HyperlinkedModelSerializer):
    """
    Abstract base serializer for models with translation support.
    """

    translated_name = SerializerMethodField()

    class Meta:
        abstract = True  # Mark this as an abstract base class

    def get_translated_name(self, obj):
        request = self.context.get("request")
        if request:
            try:
                current_language = to_locale(get_language()).replace("_", "-")
                if (
                    obj.translations
                    and isinstance(obj.translations, dict)
                    and current_language in obj.translations
                ):
                    return obj.translations.get(current_language)
                else:
                    return getattr(
                        obj, "name", ""
                    )  # Fallback to 'name' or empty string
            except AttributeError:
                return getattr(obj, "name", "")
        return getattr(obj, "name", "")


class CategorySerializer(BaseTranslationSerializer):
    # translated_name = SerializerMethodField()

    # def get_translated_name(self, obj):
    #     request = self.context.get("request")
    #     if request:
    #         try:
    #             current_language = to_locale(get_language()).replace("_", "-")
    #             print(100 * "%")
    #             print(f"current_language : {current_language}")
    #             print(100 * "%")
    #             if obj.translations and current_language in obj.translations:

    #                 return obj.translations.get(current_language)
    #             else:
    #                 return obj.name  # Fallback to the original name
    #         except AttributeError:
    #             return obj.name  # Handle cases where request might not be available
    #     return obj.name

    image = SerializerMethodField()  # Use SerializerMethodField to return the URL

    def get_image(self, obj: Category):
        if obj.firebase_image_url:
            return obj.firebase_image_url
        elif obj.image:
            # If you still want to serve local images for some reason, you can do it here
            # return self.context['request'].build_absolute_uri(obj.image.url)
            return None  # Or return None if you only want Firebase URLs
        return None

    class Meta:
        model = Category
        fields = [
            "url",
            "id",
            "name",
            "translated_name",
            "image",
            "firebase_image_url",  # Include the new field
            "translations",
            "created_at",
            "last_updated",
        ]
