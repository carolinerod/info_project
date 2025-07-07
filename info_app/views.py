<<<<<<< HEAD
import json
import platform
import socket
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import BookForm, ContactForm, PersonForm
from .models import Person, Book

class HelloWorldView(View):
    def get(self, request):
        return JsonResponse({'message': 'Hello, World!'})

class ServerInfoView(View):
    def get(self, request):
        hostname = socket.gethostname()
        python_version = platform.python_version()
        return JsonResponse({
            'python_version': python_version,
            'hostname': hostname
        })

class WelcomeView(TemplateView):
    template_name = "info_app/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name', 'Visitante')
        return context

class BookListView(ListView):
    model = Book
    template_name = "info_app/book_list.html"
    context_object_name = "books"

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "info_app/book_form.html"
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "info_app/book_form.html"
    pk_url_kwarg = "book_id"
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = "info_app/book_confirm_delete.html"
    pk_url_kwarg = "book_id"
    success_url = reverse_lazy('book_list')

class PersonListView(ListView):
    model = Person
    template_name = "info_app/person_list.html"
    context_object_name = "people"

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "info_app/person_form.html"
    success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "info_app/person_form.html"
    success_url = reverse_lazy('person_list')

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        context = {'success': True, 'name': name }
        return render(request, 'info_app/contact.html', context)
    return render(request, 'info_app/contact.html', {'form': form})
=======
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime
from django.views import View
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_name"] = "Atividade de ensino"
        context["description"] = "Trabalho part2 "
        context["year"] = now().year
        return context

#/welcome
def welcome(request):
    return JsonResponse({"message": "Welcome to the Personal Info API!"})
class WelcomeView(View):
    def get(self, request):
        return JsonResponse({"message": "Welcome to the Personal Info API!"})

# /goodbye
def goodbye(request):
    return JsonResponse({"message": "Goodbye, see you next time!"})
class GoodbyeView(View):
    def get(self, request):
        return JsonResponse({"message": "Goodbye, see you next time!"})

# /current-time
def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return JsonResponse({"current_time": now})

# /name=SeuNome
def greet(request):
    name = request.GET.get('name', 'Stranger')
    return JsonResponse({"message": f"Hello, {name}!"})

# 5️⃣ /age-category?age=XX
def age_category(request):
    age = request.GET.get('age')
    if age is None:
        return JsonResponse({"error": "Missing 'age' parameter."}, status=400)
    try:
        age = int(age)
    except ValueError:
        return JsonResponse({"error": "Invalid 'age' parameter."}, status=400)

    if 0 <= age <= 12:
        category = "Child"
    elif 13 <= age <= 17:
        category = "Teenager"
    elif 18 <= age <= 59:
        category = "Adult"
    elif age >= 60:
        category = "Senior"
    else:
        category = "Invalid age"

    return JsonResponse({"category": category})

# 6️⃣ /sum/<num1>/<num2>
def sum_numbers(request, num1, num2):
    try:
        total = int(num1) + int(num2)
        return JsonResponse({"sum": total})
    except ValueError:
        return JsonResponse({"error": "Invalid input, please provide two integers."})
   
    
        

>>>>>>> 48b606f33ff92a87352ffb733161295fbe4f4df5
