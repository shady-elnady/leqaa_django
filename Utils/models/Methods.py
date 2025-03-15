from django.db.models import Max
from os.path import join


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


def upload_image_to(instance, fileName):

    all = instance.__class__.objects.all()
    # might be possible model has no records so make sure to handle None
    next_id = all.aggregate(Max("id"))["id__max"] + 1 if all else 1

    extention = fileName.split(".")[-1]
    imgName = getattr(instance, f"{next_id}", f"{instance.name}")
    newName = f"{imgName}.{extention}"

    if instance.user:
        return str(
            join(
                "images",
                "Users",
                f"{instance.user.id}",
                f"{instance.user.id}_{newName}",
            )
        )
    elif instance.event:
        imgName = getattr(instance, f"{instance.id}", f"{instance.title}")
        return str(
            join(
                "images",
                "Events",
                f"{instance.event.id}_{newName}",
            )
        )
    else:
        return str(
            join(
                "images",
                f"{instance._meta.verbose_name_plural}".strip().replace(" ", "_"),
                newName,
            )
        )


def upload_avatar_to(instance, fileName):

    extention = fileName.split(".")[-1]
    newName = f"Avatar_{instance.user.id}.{extention}"
    return str(
        join(
            "images",
            "Users",
            f"{instance.user.id}",
            newName,
        )
    )
