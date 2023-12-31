from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from lesson2.models import Post, Author


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from class")


def posts(request, year):
    return HttpResponse(f"Posts from {year} year")


class PostsView(View):
    def get(self, request, year, month):
        return HttpResponse(f"Posts from {year}/{month}")


def posts_detail(request, year, month, slug):
    response = {
        'year': year,
        'month': month,
        'slug': slug
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'lesson3/my_template.html', context)


class TemplIf(TemplateView):
    template_name = "lesson3/if_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        # context['number'] = 3
        return context


class TemplFor(TemplateView):
    template_name = "lesson3/for_template.html"

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        my_list = ['apple', 'banana', 'orange']
        my_dict = {
            'каждый': 'красный',
            'охотник': 'оранжевый',
            'желает': 'жёлтый',
            'знать': 'зелёный',
            'где': 'голубой',
            'сидит': 'синий',
            'фазан': 'фиолетовый',
        }
        context.update({'my_list': my_list, 'my_dict': my_dict})
        return context


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = author.posts.order_by('-id')[:5]
    # posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'lesson3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'lesson3/post_full.html', {'post': post})
