from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_forms = UserCreateForm()
        return render(request, 'users/register.html', {'form': create_forms})

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {'login_form': login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have successfully out.')
        return redirect('/')


# LoginRequiredMixin  manbu yozilgan if ni orniga ishlaydi  if not request.user.is_authenticated:return redirect(
# 'users:login')
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        # {'user': request.user} bilan login qilingan userlarni olib odim
        # is_authenticated user login bolganmi yoqmi tekshiradi token tekshiradi
        # if not request.user.is_authenticated:
        #     return redirect('users:login')
        # else:
        # {'user': request.user} bilan login qilingan userlarni olib odim
        return render(request, 'users/profile.html', {'user': request.user})


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm()
        return render(request, 'users/profile_edit.html', {'update_form': user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'You have successfully updated your profile')
            return redirect('users:profile')
        else:
            return render(request, 'users/profile_edit.html', {'update_form': user_update_form})
