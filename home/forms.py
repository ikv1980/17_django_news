from django import forms
from .models import userMessage, aboutMessage


# Форма сообщений с вкладки [Контакты]
class ContactForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите ФИО:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'})
    )
    email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    phone = forms.CharField(
        label='Телефон:',
        required=False,
        help_text='Телефон вводите в любом формате',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'})
    )
    textfield = forms.CharField(
        label='Сообщение:',
        required=True,
        help_text='Введите ваше сообщение. Не более 500 символов',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите сообщение'}),
    )
    class Meta:
        model = userMessage
        fields = ['username', 'email', 'phone', 'textfield']

# Форма сообщений с вкладки [О нас]
class AboutForm(forms.ModelForm):
    subject = forms.CharField(
        label='Тема письма:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему письма'})
    )
    to_email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    plain_message = forms.CharField(
        label='Текст сообщения:',
        required=True,
        help_text='Введите ваше сообщение. Не более 500 символов',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите сообщение'}),
    )
    class Meta:
        model = aboutMessage
        fields = ['subject', 'to_email', 'plain_message']
