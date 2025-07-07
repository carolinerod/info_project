"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from info_app.views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    PersonListView,
    PersonCreateView,
    PersonUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', BookListView.as_view(), name='home'), 
    path('book/list', BookListView.as_view(), name='book_list'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/edit/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('person/list', PersonListView.as_view(), name='person_list'),
    path('person/new/', PersonCreateView.as_view(), name='person_create'),
    path('person/edit/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
]
=======

from django.contrib import admin
from django.urls import path
from info_app import views
from info_app.views import WelcomeView, GoodbyeView
from info_app.views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', views.welcome),
    path('goodbye', views.goodbye),
    path('current-time', views.current_time),
    path('greet', views.greet),
    path('age-category', views.age_category),
    path('sum/<num1>/<num2>', views.sum_numbers),
    path('welcome', WelcomeView.as_view()),
    path('goodbye', GoodbyeView.as_view()),
    path('about', AboutView.as_view()),
]
>>>>>>> 48b606f33ff92a87352ffb733161295fbe4f4df5
