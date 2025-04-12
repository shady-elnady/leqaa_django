from rest_framework.settings import api_settings


class PermissionByAction(object):

    permission_classes_by_action: dict = {
        "create": api_settings.DEFAULT_PERMISSION_CLASSES,
        "list": api_settings.DEFAULT_PERMISSION_CLASSES,
        "retrieve": api_settings.DEFAULT_PERMISSION_CLASSES,
        "destroy": api_settings.DEFAULT_PERMISSION_CLASSES,
    }

    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

        if self.action == "list":
            permission_classes = self.permission_classes_by_action["list"]

        elif self.action == "create":
            permission_classes = self.permission_classes_by_action["create"]

        elif self.action == "retrieve":
            permission_classes = self.permission_classes_by_action["retrieve"]

        elif self.action == "destroy":
            permission_classes = self.permission_classes_by_action["destroy"]

        return [permission() for permission in permission_classes]
