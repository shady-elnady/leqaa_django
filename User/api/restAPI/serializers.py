from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    Serializer,
    ModelSerializer,
    ValidationError,
    CharField,
)
from django.contrib.auth.password_validation import validate_password


from Category.api import CategorySerializer
from Organization.api import CollegeSerializer, UniversitySerializer
from User.models import User, UserAlbum, Student, Lecturer, Profile, Interest


class UserAlbumSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = UserAlbum
        fields = [
            "url",
            "id",
            "user",
            "image",
            "order",
            "created_at",
            "last_updated",
        ]


class InterestSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Interest
        fields = [
            "url",
            "id",
            # "user",
            "category",
            "order",
            "is_notifiable",
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
            # "user_type",
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
            "Specialized_to_category",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        return lecturer


class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)

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
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        # Get the user from context (set in the view)
        user = self.context["user"]
        # Create profile for the user
        return Profile.objects.create(user=user, **validated_data)


class PasswordSerializer(Serializer):
    password = CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError("Passwords don't match")
        return attrs


class UserDetailsSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "mobile",
            "is_active",
            "email_verified_at",
            "profile",  # Nested profile data
        ]
        read_only_fields = fields  # All fields are read-only
