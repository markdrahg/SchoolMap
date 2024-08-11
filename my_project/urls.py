# """
# URL configuration for my_project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """


# from django.contrib import admin
# from django.urls import path
# from my_app.views import index

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index, name='index'),
# ]



# from django.urls import path
# from my_app.views import get_books_json, index

# urlpatterns = [
#     path('', index, name='index'),
#     path('books/json/', get_books_json, name='get_books_json'),
# ]


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from my_app.views import get_books_json, index, user_page

from my_app.views import show_schools
from my_app.views import api_schools
from my_app.views import try_api

from my_app.views import save_school, unsave_school, get_saved_schools

urlpatterns = [
    path('', index, name='index'),

    path('save_school/', save_school, name='save_school'),
    path('unsave_school/', unsave_school, name='unsave_school'),
    path('api/saved_schools/', get_saved_schools, name='get_saved_schools'),

    path('user_page/', user_page, name='user_page'),
    path('show_schools/', show_schools, name='show_schools'),
    path('api/schools/', api_schools, name='api_schools'),
    path('try_page/', try_api, name='try_page'),
    path('books/json/', get_books_json, name='get_books_json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

