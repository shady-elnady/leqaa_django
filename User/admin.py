from django.contrib.admin import ModelAdmin, TabularInline, StackedInline, register
from django.template.loader import get_template
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _  # noqa: F401

from User.models import User, Profile, Student, Lecturer, Interest


class ProfileInline(
    StackedInline,  # Use admin.StackedInline for OneToOne
    # admin.TabularInline,  # Use admin.TabularInline for ForeignKey.
):
    model = Profile
    extra = 1


class InterestInline(TabularInline):
    model = Interest
    extra = 1


@register(User)
class UserAdmin(ModelAdmin):
    # form = ProfileAdminForm
    model = User
    extra = 1
    inlines = [
        ProfileInline,
    ]


@register(Student)
class StudentAdmin(ModelAdmin):
    model = Student
    extra = 1
    inlines = [
        InterestInline,
    ]


#########################################################################################


# class UserInlineForm(StackedInline.form):
#     def __init__(self, *args, **kwargs):
#         super(UserInlineForm, self).__init__(*args, **kwargs)
#         self.instance.form = self

#     def is_valid(self):
#         return super().is_valid() and self.nested.formset.is_valid()

#     @cached_property
#     def nested(self):
#         modeladmin = UserAdmin(self._meta.model, self.modeladmin.admin_site)

#         # get formsets and instances for change/add view depending on the request
#         formsets, instances = modeladmin._create_formsets(
#             self.modeladmin.request, self.instance, change=self.instance.pk
#         )

#         # gets the inline from inline_formsets
#         inline = modeladmin.get_inline_formsets(
#             self.modeladmin.request, formsets[:1], instances[:1], self.instance
#         )[0]

#         # handles prefix
#         inline.formset.prefix = f"{self.prefix}_{formsets[0].prefix}".replace("-", "_")
#         return inline

#     def is_multipart(self, *args, **kwargs):
#         return super().is_multipart() or self.nested.formset.form().is_multipart()

#     @cached_property
#     def changed_data(self):
#         changed_inline_fields = []
#         for form in self.nested.formset:
#             for name, bf in form._bound_items():
#                 if bf._has_changed():
#                     changed_inline_fields.append(name)
#         return super().changed_data + changed_inline_fields

#     def save(self, *args, **kwargs):
#         response = super().save(*args, **kwargs)
#         self.nested.formset.save(*args, **kwargs)
#         return response


# class UserInline(StackedInline):
#     extra = 1
#     model = User
#     fields = (
#         "username",
#         "mobile",
#         "Profile_inline",
#     )
#     readonly_fields = ("Profile_inline",)
#     form = UserInlineForm

#     def nick_name_inline(self, obj=None, *args, **kwargs):
#         context = getattr(self.modeladmin.response, "context_data", None) or {}
#         # insert nested inline from form
#         return get_template(obj.form.nested.opts.template).render(
#             context | {"inline_admin_formset": obj.form.nested}, self.modeladmin.request
#         )

#     def get_formset(self, *args, **kwargs):
#         formset = super().get_formset(*args, **kwargs)
#         # from.modeladmin is needed in property form.nested
#         # for nested inline
#         formset.form.modeladmin = self.modeladmin
#         return formset


# @register(Student)
# class StudentAdmin(ModelAdmin):
#     model = Student
#     extra = 1
#     inlines = [
#         UserInline,
#         InterestInline,
#     ]


# @register(Lecturer)
# class LecturerAdmin(ModelAdmin):
#     model = Lecturer
#     extra = 1
#     inlines = [
#         UserInline,
#     ]
