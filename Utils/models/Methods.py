from django.db.models import Max
from os.path import join

from User.utils.enums import USERS_TYPES


# def upload_image_to(instance, fileName):
#     extention = fileName.split(".")[-1]
#     imgName = getattr(instance, f"{instance.pk}", f"{instance.name}")
#     newName = f"{imgName}.{extention}"
#     return str(
#         join(
#             "images",
#             f"{instance._meta.verbose_name_plural}".strip().replace(" ", "_"),
#             newName,
#         )
#     )


def upload_image_to(instance, filename):

    ALL = instance.__class__.objects.all()
    # might be possible model has no records so make sure to handle None
    next_id = ALL.aggregate(Max("id"))["id__max"] + 1 if ALL else 1

    MODEL_FOLDR_NAME = f"{instance._meta.verbose_name_plural}".strip().replace("_", " ")

    if bool(getattr(instance, "user", False)):
        USER_TYPE_PATH = ""
        if instance.user.user_type == USERS_TYPES.Lecturer:
            USER_TYPE_PATH = "Lecturers"
        elif instance.user.user_type == USERS_TYPES.Student:
            USER_TYPE_PATH = "Students"
        elif instance.user.user_type == USERS_TYPES.Admin:
            USER_TYPE_PATH = "Admins"
        elif instance.user.user_type == USERS_TYPES.SuperUser:
            USER_TYPE_PATH = "Super Users"
        elif instance.user.user_type == USERS_TYPES.Staff:
            USER_TYPE_PATH = "Staff"
        elif instance.user.user_type == USERS_TYPES.Developer:
            USER_TYPE_PATH = "Developer"
        else:
            USER_TYPE_PATH = "Users"
        return str(
            join(
                "images",
                MODEL_FOLDR_NAME,
                USER_TYPE_PATH,
                f"{instance.user.id}",
                f"{getattr(instance, f"{next_id}", f"{instance.name}")}.{filename.split(".")[-1]}",
            )
        )
    elif bool(getattr(instance, "event", False)):
        return str(
            join(
                "images",
                MODEL_FOLDR_NAME,
                f"{instance.event.id}",
                f"{next_id}.{filename.split(".")[-1]}",
            )
        )
    else:
        return str(
            join(
                "images",
                MODEL_FOLDR_NAME,
                f"{next_id}.{filename.split(".")[-1]}",
            )
        )


def upload_avatar_to(instance, filename):
    USER_TYPE_PATH = ""
    if instance.user.user_type == USERS_TYPES.Lecturer:
        USER_TYPE_PATH = "Lecturers"
    elif instance.user.user_type == USERS_TYPES.Student:
        USER_TYPE_PATH = "Students"
    elif instance.user.user_type == USERS_TYPES.Admin:
        USER_TYPE_PATH = "Admins"
    elif instance.user.user_type == USERS_TYPES.SuperUser:
        USER_TYPE_PATH = "Super Users"
    elif instance.user.user_type == USERS_TYPES.Staff:
        USER_TYPE_PATH = "Staff"
    else:
        USER_TYPE_PATH = "Users"
    return join(
        "images",
        "Avatars",
        USER_TYPE_PATH,
        f"{instance.user.id}.{filename.split(".")[-1]}",
    )
