import re


def get_model_name_from_instance(instance) -> str:
    # Clean and normalize model name
    model_name = str(instance._meta.verbose_name_plural).strip()
    model_name = re.sub(r"[^\w\s-]", "", model_name)  # Remove special chars
    model_name = re.sub(
        r"[\s_]+", "-", model_name
    )  # Replace spaces/underscores with hyphens
    return model_name


def get_model_name_from_class(model_class) -> str:
    """
    Get a normalized model name from a Django model class

    Args:
        model_class: The Django model class (not instance)

    Returns:
        str: Normalized model name in lowercase with hyphens
    """
    # Clean and normalize model name
    model_name = str(model_class._meta.verbose_name_plural).strip()
    model_name = re.sub(r"[^\w\s-]", "", model_name)  # Remove special chars
    model_name = re.sub(
        r"[\s_]+", "-", model_name
    )  # Replace spaces/underscores with hyphens
    return model_name
