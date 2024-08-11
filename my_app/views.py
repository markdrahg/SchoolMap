from django.shortcuts import render
# import os
# from django.http import JsonResponse
# from django.conf import settings


# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
 


import os
import json
from django.http import JsonResponse
from django.conf import settings


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from .forms import SignUpForm, LoginForm
from .forms import SignUpForm, LoginForm
from .models.school import School
from .models.user import CustomUser



def show_schools(request):
    schools = School.objects.all()
    return render(request, 'show_schools.html', {'schools': schools})


def api_schools(request):
    schools = School.objects.all().values('name', 'acceptance_rate', 'country', 'website')
    return JsonResponse(list(schools), safe=False)



def get_books_json(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'my_project', 'books.json')
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)


# def index(request):
#     return render(request, 'index.html')
 
def user_page(request):
    schools = School.objects.all()
    return render(request, 'user_page.html', {'schools': schools})
 

def try_api(request):
    schools = School.objects.all()
    return render(request, 'try.html', {'schools': schools})



def index(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, prefix='signup')
        login_form = LoginForm(request, request.POST, prefix='login')

        if 'signup-submit' in request.POST:
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                print("Signup successful for user:", user.username)
                return redirect('user_page')
            else:
                print("Signup form invalid:", signup_form.errors)

        elif 'login-submit' in request.POST:
            if login_form.is_valid():
                print("Login form valid")
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                print("Attempting to authenticate user:", username)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    print("Login successful for user:", user.username)
                    return redirect('user_page')
                else:
                    print("Authentication failed for user:", username)
            else:
                print("Login form invalid:", login_form.errors)
                print("Submitted username:", request.POST.get('login-username'))
                print("Submitted password:", request.POST.get('login-password'))

    else:
        print("GET request received")
        signup_form = SignUpForm(prefix='signup')
        login_form = LoginForm(prefix='login')

    return render(request, 'index.html', {'signup_form': signup_form, 'login_form': login_form})








# def index(request):
#     if request.method == 'POST':
#         signup_form = SignUpForm(request.POST, prefix='signup')
#         login_form = LoginForm(request, request.POST, prefix='login')

#         if 'signup-submit' in request.POST:
#             if signup_form.is_valid():
#                 user = signup_form.save()
#                 login(request, user)
#                 print("Signup successful for user:", user.username)
#                 return redirect('user_page')
#             else:
#                 print("Signup form invalid:", signup_form.errors)

#         elif 'login-submit' in request.POST:
#             if login_form.is_valid():
#                 print("Login form valid")
#                 username = login_form.cleaned_data.get('username')
#                 password = login_form.cleaned_data.get('password')
#                 print("Attempting to authenticate user:", username)
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     print("Login successful for user:", user.username)
#                     return redirect('user_page')
#                 else:
#                     print("Authentication failed for user:", username)
#             else:
#                 print("Login form invalid:", login_form.errors)

#     else:
#         print("GET request received")
#         signup_form = SignUpForm(prefix='signup')
#         login_form = LoginForm(prefix='login')

#     return render(request, 'index.html', {'signup_form': signup_form, 'login_form': login_form})








# def index(request):
#     if request.method == 'POST':
#         signup_form = SignUpForm(request.POST, prefix='signup')
#         login_form = LoginForm(request, request.POST, prefix='login')

#         if 'signup-submit' in request.POST and signup_form.is_valid():
#             user = signup_form.save()
#             login(request, user)
#             return redirect('user_page')

#         elif 'login-submit' in request.POST and login_form.is_valid():
#                 print("Worked 1")
#                 username = login_form.cleaned_data.get('username')
#                 password = login_form.cleaned_data.get('password')
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     print("Worked 12")
#                     return redirect('user_page')
#                 else:
#                     print("user not found erorr")
#     else:
#         print("non work 22")
#         signup_form = SignUpForm(prefix='signup')
#         login_form = LoginForm(prefix='login')

#     return render(request, 'index.html', {'signup_form': signup_form, 'login_form': login_form})
