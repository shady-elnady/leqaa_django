from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    PrimaryKeyRelatedField,
    # HyperlinkedRelatedField,
)

from Category.api import CategorySerializer
from Locale.api import LanguageSerializer
from Currency.api import CurrencySerializer
from Organization.api import CollegeSerializer, UniversitySerializer
from User.models import User, UserAlbum, Student, Lecturer, Profile, Interest


class UserAlbumSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = UserAlbum
        fields = [
            "url",
            "id",
            "user",
            "photo",
            "order",
            "created_at",
            "last_updated",
        ]


class InterestSerializer(HyperlinkedModelSerializer):
    # category = CategorySerializer(many=False)
    # user = PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     required=False,  # Make category optional
    #     allow_null=True,  # make category accept null values.
    # )

    class Meta:
        model = Interest
        fields = [
            "url",
            "id",
            # "user",
            "category",
            "order",
            "created_at",
            "last_updated",
        ]
        extra_kwargs = {
            "url": {"view_name": "interest-detail"},
        }


class UserSerializer(HyperlinkedModelSerializer):
    UserPhotosAlbum = UserAlbumSerializer(many=True)
    Interests = InterestSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "uid",
            "user_type",
            "username",
            "email",
            "mobile",
            "password",
            "Interests",
            "UserPhotosAlbum",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            },
            "url": {"view_name": "user-detail"},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    university = UniversitySerializer(read_only=True)
    college = CollegeSerializer(read_only=True)
    Interests = InterestSerializer(many=True)

    class Meta:
        model = Student
        fields = [
            "user",
            "university",
            "college",
            "Interests",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student


class LecturerSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Lecturer
        fields = [
            "user",
            "category",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        return lecturer


class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    # language = LanguageSerializer(many=False)
    # currency = CurrencySerializer(many=False)

    class Meta:
        model = Profile
        fields = [
            "url",
            "id",
            "user",
            "title",
            "avatar",
            "national_id",
            "birth_date",
            "gender",
            "university_number",
            "is_graduate",
            "currency",
            "language",
            "age",
            "contact_info",
            "created_at",
            "last_updated",
        ]
