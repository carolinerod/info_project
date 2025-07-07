from django import forms

from .models import Book, Person 


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'published_date']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class': 'form-control', 'min': '10'}),
            'published_date' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
        }
        help_texts = {
            'pages': 'Informe um número inteiro maior que 10.',
            'published_date': 'Use o formato AAAA-MM-DD.'
        }
        labels = {
            'title' : 'Título do Livro',
            'author' : 'Autor do Livro',
            'pages' : 'Número de páginas',
            'published_date' : 'Data de Publicação',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['published_date'].input_formats = ['%Y-%m-%d']


class ContactForm(forms.Form):
    name = forms.CharField(label="Seu nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("O nome deve ter no mínimo 3 caracteres.")
        return name


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 150:
            raise forms.ValidationError("A idade não pode ser maior que 150 anos.")
        return age
    
    

class FeedbackForm(forms.Form):
    SATISFACTION_CHOICES = [
        ('EX', 'Excelente'),
        ('BOM', 'Bom'),
        ('REG', 'Regular'),
        ('RUI', 'Ruim'),
    ]

    name = forms.CharField(label="Seu nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    comment = forms.CharField(label="Comentário", widget=forms.Textarea)
    satisfaction = forms.ChoiceField(
        label="Nota de Satisfação",
        choices=SATISFACTION_CHOICES,
        widget=forms.RadioSelect
    )