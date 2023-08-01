from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


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
