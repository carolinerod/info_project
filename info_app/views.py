import json
import platform
import socket
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Apenas adicionei FeedbackForm a sua lista de importações original
from .forms import BookForm, ContactForm, PersonForm, FeedbackForm
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

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            satisfaction = form.cleaned_data['satisfaction']
            satisfaction_display = dict(form.fields['satisfaction'].choices)[satisfaction]
            
            context = {
                'name': name,
                'satisfaction_display': satisfaction_display
            }
            return render(request, 'info_app/feedback_success.html', context)
    else:
        form = FeedbackForm()

    return render(request, 'info_app/feedback.html', {'form': form})