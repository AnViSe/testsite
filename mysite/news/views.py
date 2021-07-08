from django.shortcuts import render, get_object_or_404



from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})