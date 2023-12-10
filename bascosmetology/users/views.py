from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import LoginUserForm, RegisterUserForm

# Create your views here.


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self) -> str:
        return reverse_lazy('home')
# def login_user(request):
#     error = ''
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         error = 'Неверные данные'
#         form = LoginUserForm()

#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'users/login.html', data)


# def logout_user(request):
#     logout(request)
#     return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # шифруем пароль из поля формы password
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})