from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy

from .utils import is_ajax, classify_face
import base64
from django.core.files.base import ContentFile

from User.models.Profile import Profile
from .models import Log

# Create your views here.

UserModel = get_user_model()


def login_view(request):
    return render(request, "Logs/login.html", {})


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("Logs:LogIn"))


@login_required
def home_view(request):
    return render(request, "main.html", {})


def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get("unknown_user_photo")
        _, str_img = photo.split(";base64")

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.image.save("upload.png", ContentFile(decoded_file))
        x.save()

        res = classify_face(x.image.path)
        if res:
            user_exists = UserModel.objects.filter(username=res).exists()
            if user_exists:
                user = UserModel.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({"success": True})
        return JsonResponse({"success": False})
