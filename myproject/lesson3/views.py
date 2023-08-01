from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView


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
