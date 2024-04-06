from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from .models import UrlData
import random
import string


def yourl(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        slug = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        new_url_data = UrlData.objects.create(url=original_url, slug=slug)
        return render(request, 'shortened_url.html', {'shortened_url': new_url_data})
    return render(request, 'yourl_form.html')

def urlRedirect(request, slug):
    url_data = UrlData.objects.get(slug=slug)
    return redirect(url_data.url)
