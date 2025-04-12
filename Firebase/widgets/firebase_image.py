from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.urls import reverse


class FirebaseImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            # Card with current image
            output.append(
                f"""
                <div class="firebase-image-card" style="margin-bottom: 20px;">
                    <div class="card" style="width: 300px;">
                        <img src="{value}" class="card-img-top" style="max-height: 200px; object-fit: contain;">
                        <div class="card-body">
                            <h5 class="card-title">Current Image</h5>
                            <input type="file" name="{name}" class="form-control" id="id_{name}">
                        </div>
                    </div>
                </div>
                """
            )
        else:
            # Just show the upload field if no image exists
            output.append(super().render(name, value, attrs, renderer))

        return mark_safe("".join(output))
