from django.shortcuts import render

import os
import json
from django.http import JsonResponse
from django.conf import settings


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
# from .forms import SignUpForm, LoginForm
from .forms import SignUpForm, LoginForm
from .models.school import School
from .models.user import CustomUser
from .models.saved_school import SavedSchool
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import logging




@csrf_exempt
def save_school(request):
    if request.method == 'POST':
        school_id = request.POST.get('school_id')
        if not school_id:
            return JsonResponse({'error': 'School ID not provided'}, status=400)

        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)

        try:
            school = get_object_or_404(School, id=school_id)
            SavedSchool.objects.get_or_create(user=user, school=school)
            return JsonResponse({'status': 'School saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt
def unsave_school(request):
    if request.method == 'POST':
        school_id = request.POST.get('school_id')
        if not school_id:
            return JsonResponse({'error': 'School ID not provided'}, status=400)

        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)

        try:
            school = get_object_or_404(School, id=school_id)
            saved_school = SavedSchool.objects.filter(user=user, school=school)
            if saved_school.exists():
                saved_school.delete()
                return JsonResponse({'status': 'School unsaved successfully'})
            else:
                return JsonResponse({'error': 'School not found in saved list'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@login_required
def get_saved_schools(request):
    user = request.user
    saved_schools = SavedSchool.objects.filter(user=user)

    data = [{
        'id': saved_school.school.id,
        'name': saved_school.school.name,
        'acceptance_rate': saved_school.school.acceptance_rate,
        'country': saved_school.school.country,
        'website': saved_school.school.website,
    } for saved_school in saved_schools]

    return JsonResponse(data, safe=False)


def show_schools(request):
    schools = School.objects.all()
    return render(request, 'show_schools.html', {'schools': schools})


def api_schools(request):
    schools = School.objects.all().values('id', 'name', 'acceptance_rate', 'country', 'website')
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

