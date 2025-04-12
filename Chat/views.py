from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def chat_view(request):
    return render(request, "Chat/chat.html")


@login_required
def other_chat_view(request):
    # # You might pass user information or initial chat data here
    context = {
        "user_id": request.user.pk,  # Or a Firebase UID if you're using Firebase Auth directly
        "firebase_config": {
            "apiKey": "AIzaSyDMvRTWSO7YWi4pD19UYqX_nFSjvCHT9EA",
            "authDomain": "wasla-fad3e.firebaseapp.com",
            "databaseURL": "https://wasla-fad3e-default-rtdb.firebaseio.com",
            "projectId": "wasla-fad3e",
            "storageBucket": "wasla-fad3e.firebasestorage.app",
            "messagingSenderId": "174924964072",
            "appId": "1:174924964072:web:a462b767388007a0ab295d",
            "measurementId": "G-N4VPTX0WPV",
        },
    }
    return render(
        request,
        "Chat/other_chat.html",
        context,
    )


@login_required
def whatss_chat_view(request):
    # # You might pass user information or initial chat data here
    context = {
        "user_id": request.user.pk,  # Or a Firebase UID if you're using Firebase Auth directly
        "firebase_config": {
            "apiKey": "AIzaSyAOQD6hoK5ECzMxFHdItTLceLKvu72PYz0",
            "authDomain": "healthy-unit.firebaseapp.com",
            "databaseURL": "https://healthy-unit-default-rtdb.firebaseio.com",
            "projectId": "healthy-unit",
            "storageBucket": "healthy-unit.appspot.com",
            "messagingSenderId": "590929307616",
            "appId": "1:590929307616:web:6603091065034b52332d85",
            "measurementId": "G-3K32G8VXVT",
        },
    }
    return render(
        request,
        "Chat/whatss_chat.html",
        context,
    )
