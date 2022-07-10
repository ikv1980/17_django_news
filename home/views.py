
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
# from requests import request
from .models import Point, News
from .forms import ContactForm, AboutForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail


# Главная страница
def home(request):
    return render(request, 'home/home.html', {'title':'Главная страница', 'topic':'Создание сайта на Django. Часть 3'})

# Услуги
def uslugi(request):
    data = {'points': Point.objects.all(), 'title':'Услуги', 'topic':'Страница с услугами'}
    return render(request, 'home/uslugi.html', data)

# О нас
def about(request):
    return render(request, 'home/about.html', {'title':'О нас', 'topic':'Немного поговорим о нас'})

# Отправка сообщения через [Контакты] просто в админку
def inputContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Сообщение отправлено')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(
        request,
        'home/contact.html',
        {
            'title': 'Контакты',
            'form': form
        }
    )

# Отправка писем через [О нас] в админку и на ящик twkostik@gmail.com
def inputAbout(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            plain_message = form.cleaned_data['plain_message']  
            from_email = form.cleaned_data['to_email']   
            to = 'ikv1980@gmail.com'
            send_mail(f'{subject} от {from_email}', plain_message, from_email, [to])
            form.save()
            messages.success(request, f'Письмо от {from_email} успешно отправлено')
            return redirect('password_reset_done')
    else:
        form = AboutForm()

    return render(
        request,
        'home/about.html',
        {
            'title': 'О нас',
            'form': form
        }
    )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Отображение всех статей из БД
class ShowNewsView(ListView):
    model = News
    template_name = 'home/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Статьи'
        ctx['topic'] = 'Простой и удобный сервис'
        return ctx

# Отображение всех статей одного автора из БД
class UserAllNewsView(ListView):
    model = News
    template_name = 'home/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')


    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx

# Отображение одной статьи из БД
class NewsDetailView(DetailView):
    model = News
    # Можно не писать строку ниже, так как по умолчанию такой путь создается автоматически
    # модель(таблица БД)_класс.
    # Если хотим свой адрес указать, то можно прописать самим типа template_name = 'home/novosti_detail.html'
    template_name = 'home/news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

# Создание статьи
class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'home/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

# Обновление существующей статьи
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'home/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

# Удаление статьи
class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'home/delete-news.html'

    def get_context_data(self, **kwards):
        ctx = super(DeleteNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Удаление статьи'
        ctx['btn_text'] = 'Да, удалить'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False
