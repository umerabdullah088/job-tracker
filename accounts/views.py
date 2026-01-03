from django.shortcuts import render
from .models import Profile
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():   # ✅ correctly nested
            print("FILES:", request.FILES)
            print("CLEANED:", form.cleaned_data)

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
             
            Profile.objects.create(
                user=user,
                profile_pic=form.cleaned_data.get("profile_pic")
            )

            return redirect("login")

    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})
